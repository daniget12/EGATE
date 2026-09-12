import os


def _normalize_database_url(url):
    if not url:
        return url
    if url.startswith("postgres://"):
        url = "postgresql+pg8000://" + url[len("postgres://") :]
    elif url.startswith("postgresql://"):
        url = "postgresql+pg8000://" + url[len("postgresql://") :]
    return url


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-secret-change-in-production"
    # NOTE: SQLite does not persist on Vercel serverless functions — the filesystem
    # is ephemeral and resets between invocations. Use DATABASE_URL with a hosted
    # database (e.g. PostgreSQL) for production deployments on Vercel.
    SQLALCHEMY_DATABASE_URI = (
        _normalize_database_url(os.environ.get("DATABASE_URL")) or "sqlite:///egate.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
