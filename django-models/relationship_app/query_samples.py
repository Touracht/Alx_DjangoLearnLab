from .models import Author, Book, Library, Librarian

books = Book.objects.filter(author_id = 'author')
books = Library.objects.all()
Librarian = Library.Librarian