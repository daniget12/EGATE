import os
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse


def _normalize_database_url(url):
    if not url:
        return url

    if url.startswith("postgres://"):
        url = "postgresql+pg8000://" + url[len("postgres://") :]
    elif url.startswith("postgresql://"):
        url = "postgresql+pg8000://" + url[len("postgresql://") :]

    parsed = urlparse(url)
    if parsed.query:
        qs = parse_qsl(parsed.query, keep_blank_values=True)
        qs = [(k, v) for k, v in qs if k not in ("sslmode", "channel_binding")]
        new_query = urlencode(qs)
        parsed = parsed._replace(query=new_query)
        url = urlunparse(parsed)

    return url


_db_uri = _normalize_database_url(os.environ.get("DATABASE_URL")) or "sqlite:///egate.db"


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-secret-change-in-production"
    # NOTE: SQLite does not persist on Vercel serverless functions — the filesystem
    # is ephemeral and resets between invocations. Use DATABASE_URL with a hosted
    # database (e.g. PostgreSQL) for production deployments on Vercel.
    SQLALCHEMY_DATABASE_URI = _db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    if _db_uri.startswith("postgresql+pg8000://"):
        SQLALCHEMY_ENGINE_OPTIONS = {"connect_args": {"ssl_context": True}}
