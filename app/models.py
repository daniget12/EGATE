from datetime import datetime, timezone

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app import db


def _utcnow():
    return datetime.now(timezone.utc)


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=True)
    github_id = db.Column(db.String(100), unique=True, nullable=True)
    discord_id = db.Column(db.String(100), unique=True, nullable=True)
    points = db.Column(db.Integer, default=0, nullable=False)
    created_at = db.Column(db.DateTime, default=_utcnow, nullable=False)
    failed_login_attempts = db.Column(db.Integer, default=0, nullable=False)
    locked_until = db.Column(db.DateTime, nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"


class Challenge(db.Model):
    __tablename__ = "challenges"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False, index=True)
    flag_hash = db.Column(db.String(256), nullable=False)
    points = db.Column(db.Integer, default=100, nullable=False)
    difficulty = db.Column(db.String(20), default="easy", nullable=False)
    hint = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=_utcnow, nullable=False)

    def set_flag(self, flag):
        self.flag_hash = generate_password_hash(flag)

    def check_flag(self, flag):
        return check_password_hash(self.flag_hash, flag)

    def __repr__(self):
        return f"<Challenge {self.title}>"


class UserChallenge(db.Model):
    __tablename__ = "user_challenges"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    challenge_id = db.Column(db.Integer, db.ForeignKey("challenges.id"), nullable=False)
    solved_at = db.Column(db.DateTime, default=_utcnow, nullable=False)

    __table_args__ = (
        db.UniqueConstraint("user_id", "challenge_id", name="_user_challenge_uc"),
    )

    def __repr__(self):
        return f"<UserChallenge user_id={self.user_id} challenge_id={self.challenge_id}>"
