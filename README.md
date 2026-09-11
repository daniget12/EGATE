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
