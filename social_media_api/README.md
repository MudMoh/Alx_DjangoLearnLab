# Social Media API

This is a Django REST Framework-based Social Media API that provides user authentication, profiles, and social features.

## Features

- User registration and login with token authentication
- Custom user model with bio and profile picture
- User profiles with follower/following counts
- Posts and comments functionality
- User follow/unfollow system
- Personalized feed showing posts from followed users
- Like/unlike posts functionality
- Notification system for likes, comments, and follows
- RESTful API endpoints with pagination and filtering

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

### Posts

- **GET** `/api/posts/` - List all posts (paginated, supports filtering and search)
  - Query params: `?page=1&page_size=10&search=keyword&author=1`
  - Returns: Paginated list of posts with comments count

- **POST** `/api/posts/` - Create a new post (requires authentication)
  - Headers: `Authorization: Token <your_token>`
  - Body: `{"title": "string", "content": "string"}`
  - Returns: Created post data

- **GET** `/api/posts/{id}/` - Get specific post with comments
  - Returns: Post data including nested comments

- **PUT/PATCH** `/api/posts/{id}/` - Update post (owner only)
  - Headers: `Authorization: Token <your_token>`
  - Body: `{"title": "string", "content": "string"}`

- **DELETE** `/api/posts/{id}/` - Delete post (owner only)
  - Headers: `Authorization: Token <your_token>`

### Comments

- **GET** `/api/comments/` - List all comments (paginated, supports filtering)
  - Query params: `?page=1&page_size=10&post=1&author=1`
  - Returns: Paginated list of comments

- **POST** `/api/comments/` - Create a new comment (requires authentication)
  - Headers: `Authorization: Token <your_token>`
  - Body: `{"post": 1, "content": "string"}`
  - Returns: Created comment data

- **GET** `/api/comments/{id}/` - Get specific comment
  - Returns: Comment data

- **PUT/PATCH** `/api/comments/{id}/` - Update comment (owner only)
  - Headers: `Authorization: Token <your_token>`
  - Body: `{"content": "string"}`

- **DELETE** `/api/comments/{id}/` - Delete comment (owner only)
  - Headers: `Authorization: Token <your_token>`

### Likes

- **POST** `/api/posts/{post_id}/like/` - Like a post (requires authentication)
  - Headers: `Authorization: Token <your_token>`
  - Returns: Success message

- **DELETE** `/api/posts/{post_id}/unlike/` - Unlike a post (requires authentication)
  - Headers: `Authorization: Token <your_token>`
  - Returns: Success message

### Follows

- **POST** `/api/accounts/follow/{user_id}/` - Follow a user (requires authentication)
  - Headers: `Authorization: Token <your_token>`
  - Returns: Success message

- **POST** `/api/accounts/unfollow/{user_id}/` - Unfollow a user (requires authentication)
  - Headers: `Authorization: Token <your_token>`
  - Returns: Success message

### Notifications

- **GET** `/api/notifications/` - Get user notifications (requires authentication)
  - Headers: `Authorization: Token <your_token>`
  - Query params: `?page=1&page_size=10`
  - Returns: Paginated list of notifications

- **POST** `/api/notifications/{notification_id}/read/` - Mark notification as read (requires authentication)
  - Headers: `Authorization: Token <your_token>`
  - Returns: Success message

### Feed

- **GET** `/api/feed/` - Get personalized feed of posts from followed users (requires authentication)
  - Headers: `Authorization: Token <your_token>`
  - Query params: `?page=1&page_size=10`
  - Returns: Paginated posts from followed users

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

## Deployment to Production

### Heroku Deployment

1. **Install Heroku CLI** and login:
   ```bash
   heroku login
   ```

2. **Create Heroku app**:
   ```bash
   heroku create your-app-name
   ```

3. **Set environment variables**:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key-here
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
   ```

4. **Deploy to Heroku**:
   ```bash
   git add .
   git commit -m "Deploy to production"
   git push heroku main
   ```

5. **Run migrations on Heroku**:
   ```bash
   heroku run python manage.py migrate
   ```

6. **Create superuser (optional)**:
   ```bash
   heroku run python manage.py createsuperuser
   ```

### Alternative Deployment Options

- **AWS Elastic Beanstalk**: Use EB CLI for deployment
- **DigitalOcean**: Use App Platform or Droplets with Docker
- **Railway**: Modern platform with Git integration

### Production Checklist

- [ ] DEBUG = False
- [ ] SECRET_KEY set via environment variables
- [ ] ALLOWED_HOSTS configured
- [ ] HTTPS enabled
- [ ] Static files collected
- [ ] Database configured
- [ ] Logging set up
- [ ] Monitoring configured
5. Create posts via POST to `/api/posts/` with token
6. View posts via GET to `/api/posts/`
7. Add comments via POST to `/api/comments/` with token
8. Filter posts by search: GET `/api/posts/?search=keyword`
9. Follow users via POST to `/api/accounts/follow/{user_id}/` with token
10. View your feed via GET to `/api/feed/` with token
11. Like posts via POST to `/api/posts/{pk}/like/` with token
12. View notifications via GET to `/api/notifications/` with token
13. Mark notifications as read via POST to `/api/notifications/{id}/read/` with token

## Project Structure

- `social_media_api/` - Main Django project
- `accounts/` - User authentication and profiles app
  - `models.py` - Custom User model
  - `serializers.py` - API serializers
  - `views.py` - API views
  - `urls.py` - URL patterns
- `posts/` - Posts and comments functionality
  - `models.py` - Post and Comment models
  - `serializers.py` - API serializers
  - `views.py` - ViewSets with permissions
  - `urls.py` - Router-based URL patterns