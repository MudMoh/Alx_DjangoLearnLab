from bookshelf.models import Book

# Retrieve the existing book instance

book = Book.objects.get(title="1984")

# Update the attribute

book.title = "Nineteen Eighty-Four"

# Save the changes to the database

book.save()

# Retrieve and show the updated title

Book.objects.get(author="George Orwell").title

```

Expected Output:
```

# 'Nineteen Eighty-Four'
