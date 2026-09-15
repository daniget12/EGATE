import os
from datetime import datetime, timedelta, timezone
from flask import Blueprint, flash, redirect, render_template, request, url_for, current_app
from flask_login import login_user, logout_user
from sqlalchemy.exc import IntegrityError
from itsdangerous import URLSafeTimedSerializer

from app import db
from app.models import User

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

def get_serializer():
    return URLSafeTimedSerializer(current_app.config['SECRET_KEY'])

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        errors = []
        if not username or len(username) < 3:
            errors.append("Username must be at least 3 characters.")
        if not email or "@" not in email:
            errors.append("A valid email address is required.")
        if len(password) < 8:
            errors.append("Password must be at least 8 characters.")
        if password != confirm_password:
            errors.append("Passwords do not match.")

        if errors:
            for message in errors:
                flash(message, "error")
            return render_template(
                "auth/register.html",
                username=username,
                email=email,
            )

        user = User(username=username, email=email)
        user.set_password(password)

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash("Username or email is already registered.", "error")
            return render_template(
                "auth/register.html",
                username=username,
                email=email,
            )

        flash("Registration successful. Please log in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_id = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        remember = request.form.get("remember") == "on"

        if "@" in login_id:
            user = User.query.filter_by(email=login_id.lower()).first()
        else:
            user = User.query.filter_by(username=login_id).first()

        if user:
            # Check brute-force protection
            if user.locked_until and user.locked_until > datetime.now(timezone.utc):
                flash(f"Account locked due to too many failed attempts. Try again after {user.locked_until.strftime('%H:%M:%S UTC')}.", "error")
                return render_template("auth/login.html", username=login_id)
            
            if user.check_password(password):
                # Login successful, reset attempts
                user.failed_login_attempts = 0
                user.locked_until = None
                db.session.commit()

                login_user(user, remember=remember)
                flash(f"Welcome back, {user.username}!", "success")
                next_page = request.args.get("next")
                return redirect(next_page or url_for("main.dashboard"))
            else:
                # Password incorrect
                user.failed_login_attempts += 1
                if user.failed_login_attempts >= 5:
                    user.locked_until = datetime.now(timezone.utc) + timedelta(minutes=15)
                    flash("Account locked for 15 minutes due to too many failed attempts.", "error")
                else:
                    flash(f"Invalid username/email or password. ({5 - user.failed_login_attempts} attempts left)", "error")
                db.session.commit()
                return render_template("auth/login.html", username=login_id)
        else:
            flash("Invalid username/email or password.", "error")
            return render_template("auth/login.html", username=login_id)

    return render_template("auth/login.html")


@auth_bp.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))


@auth_bp.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        user = User.query.filter_by(email=email).first()
        if user:
            s = get_serializer()
            token = s.dumps(user.email, salt='reset-password')
            reset_url = url_for('auth.reset_password', token=token, _external=True)
            # Simulating email send by printing to console
            print(f"\n\n--- PASSWORD RESET LINK ---\nSend this link to {user.email}:\n{reset_url}\n---------------------------\n\n")
            flash("If an account exists for that email, a reset link has been printed to the server console.", "info")
        else:
            flash("If an account exists for that email, a reset link has been printed to the server console.", "info")
        return redirect(url_for('auth.login'))
    return render_template("auth/forgot_password.html")


@auth_bp.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    s = get_serializer()
    try:
        email = s.loads(token, salt='reset-password', max_age=3600) # 1 hour
    except Exception:
        flash("The reset link is invalid or has expired.", "error")
        return redirect(url_for('auth.forgot_password'))

    if request.method == "POST":
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        if len(password) < 8:
            flash("Password must be at least 8 characters.", "error")
        elif password != confirm_password:
            flash("Passwords do not match.", "error")
        else:
            user = User.query.filter_by(email=email).first()
            if user:
                user.set_password(password)
                user.failed_login_attempts = 0
                user.locked_until = None
                db.session.commit()
                flash("Your password has been reset successfully. You can now log in.", "success")
                return redirect(url_for("auth.login"))
            else:
                flash("User not found.", "error")
                return redirect(url_for("auth.register"))
    
    return render_template("auth/reset_password.html", token=token)


@auth_bp.route("/login/github")
def github_login():
    oauth = current_app.extensions.get('oauth')
    if not oauth:
        flash("OAuth is not configured.", "error")
        return redirect(url_for('auth.login'))
    
    github = oauth.create_client('github')
    if not github:
        github = oauth.register(
            name='github',
            client_id=os.environ.get('GITHUB_CLIENT_ID'),
            client_secret=os.environ.get('GITHUB_CLIENT_SECRET'),
            access_token_url='https://github.com/login/oauth/access_token',
            access_token_params=None,
            authorize_url='https://github.com/login/oauth/authorize',
            authorize_params=None,
            api_base_url='https://api.github.com/',
            client_kwargs={'scope': 'user:email'},
        )
    
    redirect_uri = url_for('auth.github_authorize', _external=True)
    return github.authorize_redirect(redirect_uri)


@auth_bp.route("/login/github/authorize")
def github_authorize():
    oauth = current_app.extensions.get('oauth')
    github = oauth.create_client('github')
    
    try:
        token = github.authorize_access_token()
    except Exception as e:
        flash(f"GitHub login failed: {str(e)}", "error")
        return redirect(url_for('auth.login'))
        
    resp = github.get('user', token=token)
    profile = resp.json()
    
    github_id = str(profile.get('id'))
    username = profile.get('login')
    
    # Try to get email (GitHub might not return it in main profile if private)
    email = profile.get('email')
    if not email:
        # Fetch emails explicitly
        email_resp = github.get('user/emails', token=token)
        emails = email_resp.json()
        primary_email = next((e['email'] for e in emails if e.get('primary') and e.get('verified')), None)
        email = primary_email or (emails[0]['email'] if emails else None)

    if not email:
        flash("Could not retrieve email from GitHub.", "error")
        return redirect(url_for('auth.login'))

    user = User.query.filter_by(github_id=github_id).first()
    
    if not user:
        # Check if email is already taken by a non-GitHub user
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            # Link accounts (optional) or deny
            existing_user.github_id = github_id
            user = existing_user
            db.session.commit()
            flash("Linked your GitHub account to your existing profile.", "success")
        else:
            # Create new user
            base_username = username
            counter = 1
            while User.query.filter_by(username=username).first():
                username = f"{base_username}{counter}"
                counter += 1
                
            user = User(username=username, email=email, github_id=github_id)
            db.session.add(user)
            db.session.commit()
            flash(f"Welcome to EGATE, {user.username}!", "success")
    else:
        # Account locked check
        if user.locked_until and user.locked_until > datetime.now(timezone.utc):
            flash(f"Account locked. Try again after {user.locked_until.strftime('%H:%M:%S UTC')}.", "error")
            return redirect(url_for('auth.login'))
        flash(f"Welcome back, {user.username}!", "success")

    login_user(user)
    next_page = request.args.get("next")
    return redirect(next_page or url_for("main.dashboard"))


@auth_bp.route("/login/google")
def google_login():
    oauth = current_app.extensions.get('oauth')
    if not oauth:
        flash("OAuth is not configured.", "error")
        return redirect(url_for('auth.login'))
    
    google = oauth.create_client('google')
    if not google:
        google = oauth.register(
            name='google',
            client_id=os.environ.get('GOOGLE_CLIENT_ID'),
            client_secret=os.environ.get('GOOGLE_CLIENT_SECRET'),
            access_token_url='https://accounts.google.com/o/oauth2/token',
            access_token_params=None,
            authorize_url='https://accounts.google.com/o/oauth2/auth',
            authorize_params=None,
            api_base_url='https://www.googleapis.com/oauth2/v1/',
            client_kwargs={'scope': 'openid email profile'},
        )
    
    redirect_uri = url_for('auth.google_authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@auth_bp.route("/login/google/authorize")
def google_authorize():
    oauth = current_app.extensions.get('oauth')
    google = oauth.create_client('google')
    
    try:
        token = google.authorize_access_token()
    except Exception as e:
        flash(f"Google login failed: {str(e)}", "error")
        return redirect(url_for('auth.login'))
        
    resp = google.get('userinfo', token=token)
    profile = resp.json()
    
    google_id = str(profile.get('id'))
    email = profile.get('email')
    
    # Create a username from email or name
    username = profile.get('name') or profile.get('given_name') or email.split('@')[0]
    # Keep alphanumeric for simplicity
    username = "".join(c for c in username if c.isalnum())

    if not email:
        flash("Could not retrieve email from Google.", "error")
        return redirect(url_for('auth.login'))

    user = User.query.filter_by(google_id=google_id).first()
    
    if not user:
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            existing_user.google_id = google_id
            user = existing_user
            db.session.commit()
            flash("Linked your Google account to your existing profile.", "success")
        else:
            base_username = username
            counter = 1
            while User.query.filter_by(username=username).first():
                username = f"{base_username}{counter}"
                counter += 1
                
            user = User(username=username, email=email, google_id=google_id)
            db.session.add(user)
            db.session.commit()
            flash(f"Welcome to EGATE, {user.username}!", "success")
    else:
        if user.locked_until and user.locked_until > datetime.now(timezone.utc):
            flash(f"Account locked. Try again after {user.locked_until.strftime('%H:%M:%S UTC')}.", "error")
            return redirect(url_for('auth.login'))
        flash(f"Welcome back, {user.username}!", "success")

    login_user(user)
    next_page = request.args.get("next")
    return redirect(next_page or url_for("main.dashboard"))

