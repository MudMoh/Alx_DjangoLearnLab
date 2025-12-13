# Django Blog

A simple blog application built with Django, featuring user authentication, post management, and basic templates.

## Features

- User registration and login
- Profile management
- Post display
- Secure authentication with CSRF protection

## Setup

1. Install Django: `pip install django`
2. Run migrations: `python manage.py migrate`
3. Create superuser: `python manage.py createsuperuser`
4. Run server: `python manage.py runserver`

## Authentication

- **Registration**: `/register/` - Create a new account
- **Login**: `/login/` - Log in with username and password
- **Logout**: `/logout/` - Log out
- **Profile**: `/profile/` - Update email (requires login)

## Security

- All forms include CSRF tokens
- Passwords are hashed using Django's secure hashing
- Login required for profile updates

## Testing

To test the authentication system:

1. Register a new user at `/register/`
2. Log in at `/login/`
3. Access profile at `/profile/` to update email
4. Log out at `/logout/`

Ensure that unauthenticated users cannot access profile pages.

superuser:
username: admin
password: admin123
