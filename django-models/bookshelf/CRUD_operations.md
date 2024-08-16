# Contains multiple operations for manipulating data inside a table

1. create_operation: book = Book.objects.create(title = '1984', author = 'George Orwell', publication_year = 1949)
output: title = "1984"
        author = "George Orwell"
        publication_year = 1949

2. retrieve_operation: book = Book.objects.all()
output: (1984, George Orwell, 1949)

3. update_operation: book = Book.objects.update(book.title = 'Nineteen Eighty-Four')
output: title = Nineteen Eighty-Four

4. delete_operation: Book.objects.delete(book)
retrieve_operation: book = Book.objects.all()
output: []
