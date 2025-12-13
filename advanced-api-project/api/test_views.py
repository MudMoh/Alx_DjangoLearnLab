from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create test authors
        self.author1 = Author.objects.create(name='Author One')
        self.author2 = Author.objects.create(name='Author Two')
        # Create test books
        self.book1 = Book.objects.create(title='Book One', publication_year=2020, author=self.author1)
        self.book2 = Book.objects.create(title='Book Two', publication_year=2021, author=self.author2)

    def test_list_books(self):
        # Test GET /api/books/
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        # Test GET /api/books/<pk>/
        response = self.client.get(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Book One')

    def test_create_book_authenticated(self):
        # Test POST /api/books/create/ with authentication
        self.client.login(username='testuser', password='testpass')
        data = {'title': 'New Book', 'publication_year': 2022, 'author': self.author1.id}
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        # Test POST /api/books/create/ without authentication
        data = {'title': 'New Book', 'publication_year': 2022, 'author': self.author1.id}
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        # Test PUT /api/books/update/<pk>/ with authentication
        self.client.login(username='testuser', password='testpass')
        data = {'title': 'Updated Book', 'publication_year': 2020, 'author': self.author1.id}
        response = self.client.put(f'/api/books/update/{self.book1.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')

    def test_update_book_unauthenticated(self):
        # Test PUT /api/books/update/<pk>/ without authentication
        data = {'title': 'Updated Book', 'publication_year': 2020, 'author': self.author1.id}
        response = self.client.put(f'/api/books/update/{self.book1.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated(self):
        # Test DELETE /api/books/delete/<pk>/ with authentication
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(f'/api/books/delete/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        # Test DELETE /api/books/delete/<pk>/ without authentication
        response = self.client.delete(f'/api/books/delete/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_filter_books_by_publication_year(self):
        # Test filtering by publication_year
        response = self.client.get('/api/books/?publication_year=2020')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_search_books(self):
        # Test searching by title
        response = self.client.get('/api/books/?search=Book One')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_order_books(self):
        # Test ordering by publication_year
        response = self.client.get('/api/books/?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2020)
        self.assertEqual(response.data[1]['publication_year'], 2021)