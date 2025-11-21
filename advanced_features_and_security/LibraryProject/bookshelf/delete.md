from bookshelf.models import Book

# Retrieve the existing book instance (using the updated title)

book = Book.objects.get(author="George Orwell")

# Delete the instance

book.delete()

# Confirm deletion by checking all objects in the Book table

Book.objects.all()

```

Expected Output:
```

(0, {'bookshelf.Book': 1})
<QuerySet []>
