from dotenv import load_dotenv

load_dotenv()

from app import create_app

# Exposed at module level for Vercel's @vercel/python builder.
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
