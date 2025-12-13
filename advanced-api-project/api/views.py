from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

# Create your views here.

# BookListView: Handles listing all books (GET) and creating a new book (POST).
# Uses BookSerializer for serialization and IsAuthenticatedOrReadOnly for permissions.
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# BookDetailView: Handles retrieving (GET), updating (PUT/PATCH), and deleting (DELETE) a single book by ID.
# Uses BookSerializer for serialization and IsAuthenticatedOrReadOnly for permissions.
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
