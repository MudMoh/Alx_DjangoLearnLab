# Social Media API

This is a Django REST Framework-based Social Media API that provides user authentication, profiles, and social features.

## Features

- User registration and login with token authentication
- Custom user model with bio and profile picture
- User profiles with follower/following counts
- RESTful API endpoints

## Setup Instructions

1. **Install Dependencies:**
   ```bash
   pip install django djangorestframework
   ```

2. **Navigate to the project directory:**
   ```bash
   cd social_media_api
   ```

3. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication

- **POST** `/api/accounts/register/` - Register a new user
  - Body: `{"username": "string", "email": "string", "password": "string", "bio": "string (optional)", "profile_picture": "file (optional)"}`
  - Returns: User data and authentication token

- **POST** `/api/accounts/login/` - Login user
  - Body: `{"username": "string", "password": "string"}`
  - Returns: User data and authentication token

- **GET** `/api/accounts/profile/` - Get user profile (requires authentication)
  - Headers: `Authorization: Token <your_token>`
  - Returns: User profile data including followers and following counts

## User Model

The custom User model extends Django's AbstractUser with:
- `bio`: Text field for user biography
- `profile_picture`: Image field for profile pictures
- `followers`: Many-to-many relationship for followers

## Testing with Postman

1. Register a new user via POST to `/api/accounts/register/`
2. Use the returned token in the Authorization header for authenticated requests
3. Login via POST to `/api/accounts/login/` to get a token
4. Access profile via GET to `/api/accounts/profile/` with token

## Project Structure

- `social_media_api/` - Main Django project
- `accounts/` - User authentication and profiles app
  - `models.py` - Custom User model
  - `serializers.py` - API serializers
  - `views.py` - API views
  - `urls.py` - URL patterns