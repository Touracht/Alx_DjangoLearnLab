1. ListView - This is a list view which is responsible for listing all the book instances. These intances
are listed in the Django Rest Framework endpoints. It includes a queryset 'Book.objects.all() to
fetch all model instances, serializer_class 'BookSerializer' which serializes all the Book model fields
and lastly, permission_class '[IsAuthenticatedOrReadOnly] which gives the read only permission to 
both authenticated and unauthenticated users.

2. DetailView - This is a detail view that uses an overriden method to retrieve a certain book instance by its primary
key in order to display its details and return a custom exception message if the book does not exist.
It also includes a permission_class '[IsAuthenticatedOrReadOnly] which gives the read only permission
to both authenticated and unauthenticated users.

3. CreateView - This is a create view which is responsible for creating Book model instances using the DRF endpoints.
It also includes a permission class which allowes only authenticated users to create the instances.

4. UpdateView - This is an update view which is responsible for updating a book instance by its primary key.
It also includes a permission class which allowes only authenticated users to update existing books.

5. DeleteView - This is an update view which is responsible for deleting a book instance by its primary key.
It also includes a permission class which allowes only authenticated users to delete existing books.