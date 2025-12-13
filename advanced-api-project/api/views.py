from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Book
from .serializers import BookSerializer

# Create your views here.

# BookListView: Handles listing all books (GET).
# Uses BookSerializer for serialization and AllowAny for permissions (read-only for all).
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

# BookDetailView: Handles retrieving a single book by ID (GET).
# Uses BookSerializer for serialization and AllowAny for permissions (read-only for all).
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

# BookCreateView: Handles creating a new book (POST).
# Uses BookSerializer for serialization and IsAuthenticated for permissions.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# BookUpdateView: Handles updating an existing book (PUT/PATCH).
# Uses BookSerializer for serialization and IsAuthenticated for permissions.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# BookDeleteView: Handles deleting a book (DELETE).
# Uses BookSerializer for serialization and IsAuthenticated for permissions.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
