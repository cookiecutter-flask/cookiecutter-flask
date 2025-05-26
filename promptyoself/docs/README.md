# PromptYoSelf Documentation

This directory contains documentation, schema diagrams, and onboarding notes for the PromptYoSelf Flask application.

## Contents

### Schema Diagrams
- `database_schema.md` - Database entity relationship diagrams
- `api_schema.md` - API endpoint documentation
- `architecture.md` - Application architecture overview

### Onboarding
- `development_setup.md` - Local development environment setup
- `deployment_guide.md` - Production deployment instructions
- `contributing.md` - Guidelines for contributors

### API Documentation
- `api_endpoints.md` - Complete API reference
- `authentication.md` - Authentication and authorization
- `rate_limiting.md` - Rate limiting policies

## Quick Start

1. **Development Setup**: See `development_setup.md`
2. **API Reference**: See `api_endpoints.md`
3. **Database Schema**: See `database_schema.md`

## Architecture Overview

PromptYoSelf follows a modular Flask application structure:

```
app/
├── api/           # API endpoints and logic
├── ui/            # Web interface views
├── jobs/          # Background job definitions
├── models.py      # Database models
├── forms.py       # WTForms definitions
└── extensions.py  # Flask extension initialization
```

## Contributing

Please read `contributing.md` before making changes to the application.
