from django.shortcuts import render
from rest_framework import generics
from .models import Book, Author
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DetailView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_book(self, response, pk):
        try:
            book = Book.objects.all(pk = pk)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        
        except Book.DoesNotExist:
            return Response('Book not found.')

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]





