# Comments Project

A Django-based web application that provides a commenting system with user authentication using JWT tokens and complete API documentation.

## Features

- User registration and authentication
- JWT token-based authentication
- Comment creation and management
- RESTful API
- API documentation via Swagger UI
- Modern responsive UI

## Prerequisites

- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone this repository:
```
git clone <repository-url>
cd comments-project
```

2. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```
pip install -r comment_project/requirements.txt
```

## Configuration

1. Navigate to the project directory:
```
cd comment_project
```

2. Run migrations to set up the database:
```
python manage.py makemigrations
python manage.py migrate
```

3. Create a superuser (admin):
```
python manage.py createsuperuser
```

4. Run the development server:
```
python manage.py runserver
```

## Usage

### Web Interface

1. Access the application at: http://127.0.0.1:8000/
2. Register a new account or log in with your credentials
3. Create and manage comments through the web interface

### API Authentication

The application uses JWT tokens for API authentication:

1. Obtain a JWT token:
```
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

2. This returns an access and refresh token:
```json
{
  "access": "your_access_token...",
  "refresh": "your_refresh_token..."
}
```

3. Use the access token in API requests:
```
curl -H "Authorization: Bearer your_access_token..." http://127.0.0.1:8000/api/endpoint/
```

4. Refresh the token when it expires:
```
curl -X POST http://127.0.0.1:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "your_refresh_token..."}'
```

### API Documentation

The complete API documentation is available through Swagger UI:

- Swagger UI: http://127.0.0.1:8000/swagger/
- ReDoc UI (alternative): http://127.0.0.1:8000/redoc/

### User Management

- Register new users: http://127.0.0.1:8000/api/auth/register/
- View user profile: http://127.0.0.1:8000/api/auth/profile/

## Project Structure

```
comment_project/
├── comment_project/      # Project settings
│   ├── settings.py       # Django settings
│   ├── urls.py           # Main URL routing
│   └── ...
├── authentication/       # User auth app
│   ├── views.py          # Auth views
│   ├── urls.py           # Auth URLs
│   └── ...
├── comments/             # Comments app
│   ├── views.py          # Comment views
│   ├── models.py         # Comment models
│   └── ...
├── templates/            # HTML templates
├── static/               # CSS, JS, images
└── ...
```

## Dependencies

- Django 5.2.3
- Django REST Framework 3.16.0
- djangorestframework-simplejwt 5.5.0
- drf-yasg 1.21.10 (for Swagger)
- Other dependencies listed in requirements.txt

## License

This project is licensed under the MIT License - see the LICENSE file for details.
