# Django Blog

A simple blog application built with Django, featuring user authentication, post management, and basic templates.

## Features

- User registration and login
- Profile management
- Post display and CRUD operations
- Comment system for posts
- Secure authentication with CSRF protection
- Author-only editing and deletion of posts and comments

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

## Blog Posts

- **List Posts**: `/posts/` - View all posts
- **View Post**: `/post/<id>/` - View a specific post
- **Create Post**: `/post/new/` - Create a new post (requires login)
- **Edit Post**: `/post/<id>/update/` - Edit a post (author only)
- **Delete Post**: `/post/<id>/delete/` - Delete a post (author only)
- **Edit Comment**: `/comment/<id>/edit/` - Edit a comment (author only)
- **Delete Comment**: `/comment/<id>/delete/` - Delete a comment (author only)

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
