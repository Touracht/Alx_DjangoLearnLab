from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """This serializer is for converting the Book model instances into python code that will 
    easly be converted into more human readable formats like JSON and XML. It serializes
    all the fields from the Book model as well and adds a validation method to handle the year
    field so it is not in future."""

    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):

        current_year = datetime.now().year

        if data['publication_year'] > current_year:
            raise serializers.ValidationError('Publication year must be current.')
        return data

class AuthorSerializer(serializers.ModelSerializer):
    """This serializer is for converting Book model instances into python code that will 
    easly be converted into more human readable formats like JSON and XML. It includes an
    additional 'books' field which is responsible for showing all the books that belong to the paricular author"""
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['name', 'books']

"""The relationship between the Author and the Book models in my serializers is handled by an additional field
'books' which is able to show books that have been created by a particular author"""


        