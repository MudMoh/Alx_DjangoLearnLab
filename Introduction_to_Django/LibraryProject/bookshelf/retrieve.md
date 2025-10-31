from bookshelf.models import Book

# Assuming the book created in the previous step is the first/only book

book = Book.objects.get(title="1984")
print(book.title)
print(book.author)
print(book.publication_year)

```

Expected Output:
```

# 1984

# George Orwell

# 1949
