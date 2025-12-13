from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

# URL patterns for the api app.
# /books/ : List all books (GET)
# /books/<int:pk>/ : Retrieve a specific book by ID (GET)
# /books/create/ : Create a new book (POST)
# /books/<int:pk>/update/ : Update a specific book (PUT/PATCH)
# /books/<int:pk>/delete/ : Delete a specific book (DELETE)
urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]