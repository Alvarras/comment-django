# Comments Project

A Django-based web application that provides a commenting system with user authentication using JWT tokens and complete API documentation.

## Features

- User registration and authentication (web & API)
- JWT token-based authentication for API
- Comment and post creation, editing, and deletion (web & API)
- RESTful API for posts and comments
- API documentation via Swagger UI
- Modern responsive UI
- **All main features require login (web protected)**

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
2. **You must register or login to access any main feature.**
3. After login, you can create, edit, and delete posts and comments.
4. Logout via the header menu.

#### Web Endpoints:
- Register: `/register/`
- Login: `/login/`
- Logout: `/logout/` (POST only, via header button)
- Home (list posts): `/` (login required)
- Post detail: `/post/<id>/` (login required)

### User Registration & Authentication (API)

- Register: 
```
POST http://127.0.0.1:8000/api/auth/register/
Content-Type: application/json
{
  "username": "your_username",
  "email": "your_email@example.com",
  "password": "your_password"
}
```

- Login (Get JWT Token): 
```
POST http://127.0.0.1:8000/api/token/
Content-Type: application/json
{
  "username": "your_username",
  "password": "your_password"
}
```

- Refresh JWT Token:
```
POST http://127.0.0.1:8000/api/token/refresh/
Content-Type: application/json
{
  "refresh": "your_refresh_token..."
}
```

- Get current user info (session):
```
GET http://127.0.0.1:8000/api/auth/me/  (requires login session)
```

### API Authentication

The application uses JWT tokens for API authentication:

1. Obtain a JWT token at `/api/token/`:
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
curl -H "Authorization: Bearer your_access_token..." http://127.0.0.1:8000/api/comments/posts/
```

4. Refresh the token when it expires:
```
curl -X POST http://127.0.0.1:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "your_refresh_token..."}'
```

### API Documentation

The complete API documentation is available at:

- Swagger UI: http://127.0.0.1:8000/api/docs/
- ReDoc UI: http://127.0.0.1:8000/api/redoc/

### CRUD Operations for Posts and Comments (API)

All endpoints below require JWT authentication (see above):

**Posts:**
- List all posts: `GET /api/comments/posts/`
- Create new post: `POST /api/comments/posts/`
- Get post detail: `GET /api/comments/posts/{id}/`
- Update post: `PUT /api/comments/posts/{id}/`
- Delete post: `DELETE /api/comments/posts/{id}/`

**Comments:**
- List all comments: `GET /api/comments/comments/`
- Create new comment: `POST /api/comments/comments/`
- Get comment detail: `GET /api/comments/comments/{id}/`
- Update comment: `PUT /api/comments/comments/{id}/`
- Delete comment: `DELETE /api/comments/comments/{id}/`

Example API request with JWT authentication:
```
curl -X POST http://127.0.0.1:8000/api/comments/comments/ \
  -H "Authorization: Bearer your_access_token..." \
  -H "Content-Type: application/json" \
  -d '{"post": 1, "content": "This is my comment"}'
```

### User Management (API)

- Register new users: http://127.0.0.1:8000/api/auth/register/
- View user info: http://127.0.0.1:8000/api/auth/me/

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
- Django REST Framework
- djangorestframework-simplejwt
- drf-yasg (for Swagger)
- Other dependencies listed in requirements.txt

## License

This project is licensed under the MIT License - see the LICENSE file for details.
