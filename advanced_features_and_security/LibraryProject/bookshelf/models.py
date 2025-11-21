from django.db import models

# Create your models here.
class Book(models.Model):
    """
    Defines the Book model for the bookshelf application.

    Attributes:
        title (str): The title of the book (max 200 characters).
        author (str): The author of the book (max 100 characters).
        publication_year (int): The year the book was published.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        # This method is used for human-readable representation,
        # often shown in the Django Admin or when printing the object.
        return f"{self.title} by {self.author} ({self.publication_year})"
