# Flask environment variables
# These are automatically loaded by python-dotenv when Flask starts

FLASK_APP=app:create_app
FLASK_ENV=development
DATABASE_URL=sqlite:///instance/dev.sqlite3
API_URL=http://localhost:5000

# Development settings
FLASK_DEBUG=1
SECRET_KEY=dev-secret-key-change-in-production

# Database settings
SQLALCHEMY_TRACK_MODIFICATIONS=False

# Cache settings
CACHE_TYPE=simple

# Security settings (development only)
WTF_CSRF_ENABLED=True
