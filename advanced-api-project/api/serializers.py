from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):

        current_year = datetime.now().year

        if data['publication_year'] > current_year:
            raise serializers.ValidationError('Publication year must me current.')

class AuthorSerializer(serializers.AuthorSerializer):
    books = BookSerializer(many = True)
    
    class Meta:
        model = Author
        fields = ['name', 'books']


        