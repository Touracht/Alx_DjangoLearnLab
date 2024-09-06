from django.db import models

class Author(models.Model):
    """This model is for creating authors who are are able to create books using the book model below.
    Each author will be identified by their unique key together with their name."""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    """This model is for creating book objects with auto_generated keys, title, publication_year and lastly the author
    field which references to the Author model as a foreign key. This will ensure that each author can create
    multiple books."""
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


