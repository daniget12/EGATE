from flask import Blueprint, render_template
from flask_login import current_user, login_required

from app.models import Challenge, User

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    if current_user.is_authenticated:
        challenge_count = Challenge.query.count()
        return render_template("dashboard.html", challenge_count=challenge_count)
    return render_template("index.html")


@main_bp.route("/dashboard")
@login_required
def dashboard():
    challenge_count = Challenge.query.count()
    return render_template("dashboard.html", challenge_count=challenge_count)


@main_bp.route("/leaderboard")
@login_required
def leaderboard():
    top_users = User.query.order_by(User.points.desc()).limit(10).all()
    return render_template("leaderboard.html", top_users=top_users)


@main_bp.route("/learning_path")
@login_required
def learning_path():
    return render_template("learning_path.html")


@main_bp.route("/robots.txt")
def robots():
    from flask import Response
    return Response("User-agent: *\nDisallow: /egate{r0b0ts_txt_1s_pUbl1c}\n", mimetype="text/plain")
