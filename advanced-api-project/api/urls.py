from django.urls import path
from .views import BookListView, BookDetailView

# URL patterns for the api app.
# /books/ : List all books (GET) and create a new book (POST)
# /books/<int:pk>/ : Retrieve (GET), update (PUT/PATCH), or delete (DELETE) a specific book by ID
urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]