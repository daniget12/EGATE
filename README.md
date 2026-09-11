# EGATE Talent Center

Cybersecurity learning platform for EGATE Talent Center — CTF challenges, progress tracking, and structured learning paths.

## Prerequisites

- Python 3.10 or newer
- pip

## Setup

1. **Create and activate a virtual environment**

   ```powershell
   cd c:\EGATE
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. **Install dependencies**

   ```powershell
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   ```powershell
   copy .env.example .env
   ```

   Edit `.env` and set a strong random value for `SECRET_KEY`.

4. **Add the EGATE logo**

   Place your logo file at:

   ```
   app/static/images/egate-logo.png
   ```

   A placeholder logo is included for development. Replace it with the official EGATE logo when available.

## Run the Application

```powershell
python run.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Current Features

- User registration with input validation
- Secure login/logout with session management (Flask-Login)
- Password hashing via Werkzeug (`pbkdf2:sha256`)
- SQLite database with `User` and `Challenge` models
- Dashboard showing points and challenge count

## Project Structure

```
EGATE/
├── app/
│   ├── __init__.py          # Application factory
│   ├── models.py            # User and Challenge models
│   ├── auth/
│   │   └── routes.py        # Registration, login, logout
│   ├── main/
│   │   └── routes.py        # Home and dashboard
│   ├── templates/           # Jinja2 HTML templates
│   └── static/
│       ├── css/style.css
│       └── images/egate-logo.png
├── config.py
├── run.py
├── requirements.txt
└── .env.example
```

## Routes

| Route              | Description              |
|--------------------|--------------------------|
| `/`                | Landing page / dashboard |
| `/auth/register`   | Create a new account     |
| `/auth/login`      | Sign in                  |
| `/auth/logout`     | Sign out                 |
| `/dashboard`       | User dashboard (login required) |

## Deployment to Vercel

### SQLite limitation on serverless

Vercel runs Python as **serverless functions** with an **ephemeral filesystem**. SQLite data stored locally (including the fallback at `/tmp/egate.db`) **does not persist** between deployments or cold starts. User accounts and challenge data will be lost when the function recycles.

For a production deployment, set `DATABASE_URL` to a hosted database such as PostgreSQL (e.g. Neon, Supabase, or Railway). Without `DATABASE_URL`, the app falls back to SQLite for local development only.

### Deploy on vercel.com

1. Push this repository to GitHub (or GitLab/Bitbucket).
2. Go to [vercel.com](https://vercel.com) and sign in.
3. Click **Add New → Project** and import your repository.
4. Vercel detects `vercel.json` and uses the `@vercel/python` builder with `run.py` as the entry point. No custom build command is required.
5. Under **Environment Variables**, add:
   - `SECRET_KEY` — a long random string (required for session security).
   - `DATABASE_URL` — (recommended) a hosted PostgreSQL connection string for persistent storage.
6. Click **Deploy**.

After deployment, your app will be available at the `*.vercel.app` URL shown in the dashboard.

### Running locally after Vercel setup

Local development is unchanged. Vercel-specific paths (`/tmp/egate.db`) apply only when the `VERCEL` environment variable is set by the platform.

```powershell
cd c:\EGATE
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
# Edit .env — set SECRET_KEY; leave DATABASE_URL unset to use local sqlite:///egate.db
python run.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.
