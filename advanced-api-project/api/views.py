from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import NotFound
from .filters import BookFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework

class ListView(generics.ListAPIView):

    """
    This is a list view which is responsible for listing all the book instances. These intances
    are listed in the Django Rest Framework endpoints. It includes a queryset 'Book.objects.all() to
    fetch all model instances, serializer_class 'BookSerializer' which serializes all the Book model fields
    and lastly, permission_class '[IsAuthenticatedOrReadOnly] which gives the read only permission to 
    both authenticated and unauthenticated users."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['title', 'publication_year']
    search_fields = ['title', 'author__name']


class DetailView(generics.GenericAPIView):

    """This is a detail view that uses an overriden method to retrieve a certain book instance by its primary
    key in order to display its details and return a custom exception message if the book does not exist.
    It also includes a permission_class '[IsAuthenticatedOrReadOnly] which gives the read only permission
    to both authenticated and unauthenticated users."""

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, response, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        
        except Book.DoesNotExist:
            raise NotFound('Book not found.')

class CreateView(generics.CreateAPIView):

    """This is a create view which is responsible for creating Book model instances using the DRF endpoints.
    It also includes a permission class which allowes only authenticated users to create the instances."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class UpdateView(generics.RetrieveUpdateAPIView):

    """This is an update view which is responsible for updating a book instance by its primary key.
    It also includes a permission class which allowes only authenticated users to update existing books."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class DeleteView(generics.RetrieveDestroyAPIView):

    """This is an update view which is responsible for deleting a book instance by its primary key.
    It also includes a permission class which allowes only authenticated users to delete existing books."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]





