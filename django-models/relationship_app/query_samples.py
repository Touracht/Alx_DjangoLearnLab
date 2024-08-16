from .models import Author, Book, Library, Librarian

books = Book.objects.filter(author_id = 'author')
books = "Library.objects.get(name=library_name)"
Librarian = Library.Librarian