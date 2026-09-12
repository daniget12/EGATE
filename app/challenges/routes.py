from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.models import Challenge, UserChallenge, db

challenges_bp = Blueprint("challenges", __name__, url_prefix="/challenges")

@challenges_bp.route("/")
@login_required
def list_challenges():
    challenges = Challenge.query.all()
    # Get solved challenge IDs for current user
    solved_ids = {uc.challenge_id for uc in UserChallenge.query.filter_by(user_id=current_user.id).all()}
    return render_template("challenges.html", challenges=challenges, solved_ids=solved_ids)

@challenges_bp.route("/<int:id>")
@login_required
def detail(id):
    challenge = db.session.get(Challenge, id)
    if not challenge:
        flash("Challenge not found.", "danger")
        return redirect(url_for("challenges.list_challenges"))
    
    is_solved = UserChallenge.query.filter_by(user_id=current_user.id, challenge_id=challenge.id).first() is not None
    return render_template("challenge_detail.html", challenge=challenge, is_solved=is_solved)

@challenges_bp.route("/<int:id>/submit", methods=["POST"])
@login_required
def submit(id):
    challenge = db.session.get(Challenge, id)
    if not challenge:
        flash("Challenge not found.", "danger")
        return redirect(url_for("challenges.list_challenges"))

    flag = request.form.get("flag", "")
    
    # Check if already solved
    existing = UserChallenge.query.filter_by(user_id=current_user.id, challenge_id=challenge.id).first()
    
    if challenge.check_flag(flag):
        if existing:
            flash("You already solved this challenge.", "info")
        else:
            uc = UserChallenge(user_id=current_user.id, challenge_id=challenge.id)
            current_user.points += challenge.points
            db.session.add(uc)
            db.session.commit()
            flash("Correct! Points awarded.", "success")
    else:
        flash("Incorrect flag. Try again.", "danger")
        
    return redirect(url_for("challenges.detail", id=challenge.id))
