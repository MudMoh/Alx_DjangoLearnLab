# Django Shell CRUD Operations for Book Model

## Create Operation

```python
from bookshelf.models import Book
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

Expected Output:

```
<Book: Book object (1)>
```

## Retrieve Operation

```python
from bookshelf.models import Book
Book.objects.get(title="1984")
```

Expected Output:

```
<Book: Book object (1)>
```

## Update Operation

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
```

Expected Output:

```
# No explicit output, but the title is updated in the database.
# You can retrieve the book again to verify.
```

## Delete Operation

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
```

Expected Output:

```
(0, {'bookshelf.Book': 1})
<QuerySet []>
```
