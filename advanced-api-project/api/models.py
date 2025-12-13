from django.db import models

# The Author model represents an author in the system.
# It has a name field to store the author's name.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# The Book model represents a book written by an author.
# It has a title, publication year, and a foreign key to the Author model,
# establishing a one-to-many relationship from Author to Books.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
