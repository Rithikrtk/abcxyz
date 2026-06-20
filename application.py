import os

from app import app, init_db

# Compatibility entrypoint for platforms that expect application:app
application = app

if __name__ == "__main__":
    # Ensure database tables exist when running directly
    init_db()
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
