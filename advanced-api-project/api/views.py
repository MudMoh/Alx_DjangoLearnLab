from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework import filters
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer

# Create your views here.

# BookListView: Custom view using ListModelMixin for listing all books (GET).
# Uses BookSerializer for serialization and AllowAny for permissions (read-only for all).
# Includes filtering by title, author, publication_year; searching on title and author name; ordering by title and publication_year.
class BookListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# BookDetailView: Custom view using RetrieveModelMixin for retrieving a single book by ID (GET).
# Uses BookSerializer for serialization and AllowAny for permissions (read-only for all).
class BookDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

# BookCreateView: Custom view using CreateModelMixin for creating a new book (POST).
# Uses BookSerializer for serialization and IsAuthenticated for permissions.
class BookCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# BookUpdateView: Custom view using UpdateModelMixin for updating an existing book (PUT/PATCH).
# Uses BookSerializer for serialization and IsAuthenticated for permissions.
class BookUpdateView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

# BookDeleteView: Custom view using DestroyModelMixin for deleting a book (DELETE).
# Uses BookSerializer for serialization and IsAuthenticated for permissions.
class BookDeleteView(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
