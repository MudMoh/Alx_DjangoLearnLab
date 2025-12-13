from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Book
from .serializers import BookSerializer

# Create your views here.

# BookListView: Custom view using ListModelMixin for listing all books (GET).
# Uses BookSerializer for serialization and AllowAny for permissions (read-only for all).
class BookListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

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
