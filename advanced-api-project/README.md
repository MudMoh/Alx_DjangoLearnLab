# Advanced API Project

This Django project demonstrates advanced API development using Django REST Framework, focusing on custom serializers and generic views.

## Models

- **Author**: Represents an author with a name field.
- **Book**: Represents a book with title, publication_year, and a foreign key to Author.

## Serializers

- **BookSerializer**: Serializes all fields of the Book model, with custom validation ensuring publication_year is not in the future.
- **AuthorSerializer**: Serializes the name and nested books using BookSerializer.

## Views

- **BookListView**: Custom view using ListModelMixin for listing all books (GET). Allows access to all users. Supports filtering by title, author, publication_year; searching on title and author name; ordering by title and publication_year.
- **BookDetailView**: Custom view using RetrieveModelMixin for retrieving a single book by ID (GET). Allows access to all users.
- **BookCreateView**: Custom view using CreateModelMixin for creating new books (POST). Requires authentication.
- **BookUpdateView**: Custom view using UpdateModelMixin for updating existing books (PUT/PATCH). Requires authentication.
- **BookDeleteView**: Custom view using DestroyModelMixin for deleting books (DELETE). Requires authentication.

## Permissions

- Read views (List and Detail) use `AllowAny` permission.
- Write views (Create, Update, Delete) use `IsAuthenticated` permission.

## URLs

- `/api/books/`: List all books (GET).
- `/api/books/<int:pk>/`: Retrieve a specific book (GET).
- `/api/books/create/`: Create a new book (POST).
- `/api/books/update/<int:pk>/`: Update a specific book (PUT/PATCH).
- `/api/books/delete/<int:pk>/`: Delete a specific book (DELETE).

## Query Parameters

The book list endpoint supports the following query parameters:

- **Filtering**: `?title=<value>`, `?author=<id>`, `?publication_year=<year>`
- **Searching**: `?search=<query>` (searches in title and author name)
- **Ordering**: `?ordering=<field>` (fields: title, publication_year; use - for descending, e.g., ?ordering=-publication_year)

Examples:
- `/api/books/?publication_year=2020`
- `/api/books/?search=Test`
- `/api/books/?ordering=title`

## Testing

- GET requests work without authentication.
- POST, PUT, PATCH, DELETE require authentication.
- Serializer validation prevents future publication years.

## Testing

The project includes comprehensive unit tests for the API endpoints in `api/test_views.py`.

### Running Tests

Run the test suite using Django's manage.py command:

```bash
python manage.py test api.test_views
```

### Test Coverage

The tests cover:
- CRUD operations: Creating, retrieving, updating, and deleting books.
- Filtering: By publication_year.
- Searching: In title and author name.
- Ordering: By title and publication_year.
- Permissions: Authenticated vs. unauthenticated access for different endpoints.

All tests use a separate test database and should pass without issues.

## Setup

1. Install dependencies: `pip install django djangorestframework django-filter`
2. Run migrations: `python manage.py migrate`
3. Run server: `python manage.py runserver`
4. Access API at `http://127.0.0.1:8000/api/`

user: admin
password: admin123

