import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-secret-change-in-production"
    # NOTE: SQLite does not persist on Vercel serverless functions — the filesystem
    # is ephemeral and resets between invocations. Use DATABASE_URL with a hosted
    # database (e.g. PostgreSQL) for production deployments on Vercel.
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///egate.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
