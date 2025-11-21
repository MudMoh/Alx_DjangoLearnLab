import os
import django
import sys
from pathlib import Path

# Add the parent directory of 'LibraryProject' to the Python path
# This allows Django to find 'LibraryProject.settings'
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Clear existing data to ensure a clean slate for sample data
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    # Create sample data
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="Stephen King")

    book1 = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author1)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3 = Book.objects.create(title="It", author=author2)
    book4 = Book.objects.create(title="The Shining", author=author2)

    library1 = Library.objects.create(name="Central Library")
    library1.books.add(book1, book3)

    library2 = Library.objects.create(name="City Archives")
    library2.books.add(book2, book4)

    librarian1 = Librarian.objects.create(name="Alice", library=library1)
    librarian2 = Librarian.objects.create(name="Bob", library=library2)

    print("--- Sample Data Created ---")

    # Query all books by a specific author
    print("\n--- Query 1: Books by J.K. Rowling ---")
    jk_rowling_books = Book.objects.filter(author__name="J.K. Rowling")
    for book in jk_rowling_books:
        print(f"  - {book.title}")

    # List all books in a library
    print("\n--- Query 2: Books in Central Library ---")
    library_name = "Central Library"
    central_library = Library.objects.get(name=library_name)
    for book in central_library.books.all():
        print(f"  - {book.title}")

    # Retrieve the librarian for a library
    print("\n--- Query 3: Librarian for Central Library ---")
    central_library_librarian = Librarian.objects.get(library=central_library)
    print(f"  - {central_library_librarian.name}")

if __name__ == '__main__':
    run_queries()
