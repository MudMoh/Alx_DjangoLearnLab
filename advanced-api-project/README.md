# Advanced API Project

This Django project demonstrates advanced API development using Django REST Framework, focusing on custom serializers and generic views.

## Models

- **Author**: Represents an author with a name field.
- **Book**: Represents a book with title, publication_year, and a foreign key to Author.

## Serializers

- **BookSerializer**: Serializes all fields of the Book model, with custom validation ensuring publication_year is not in the future.
- **AuthorSerializer**: Serializes the name and nested books using BookSerializer.

## Views

- **BookListView**: A generic ListCreateAPIView for listing all books (GET) and creating new books (POST). Requires authentication for POST.
- **BookDetailView**: A generic RetrieveUpdateDestroyAPIView for retrieving, updating, and deleting individual books by ID. Requires authentication for write operations.

## Permissions

All views use `IsAuthenticatedOrReadOnly` permission, allowing unauthenticated users to read data but requiring authentication for create, update, and delete operations.

## URLs

- `/api/books/`: Book list and create endpoint.
- `/api/books/<int:pk>/`: Book detail, update, and delete endpoint.

## Testing

- GET requests work without authentication.
- POST, PUT, PATCH, DELETE require authentication.
- Serializer validation prevents future publication years.

## Setup

1. Install dependencies: `pip install django djangorestframework`
2. Run migrations: `python manage.py migrate`
3. Run server: `python manage.py runserver`
4. Access API at `http://127.0.0.1:8000/api/`

user: admin
password: admin123

