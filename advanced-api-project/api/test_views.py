from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Book

class APITestCase(TestCase):
    def setUp(self):
        
        self.client = APIClient()

        self.book1 = Book.objects.create(title='Book One', author='Author A', publication_year=2020)
        self.book2 = Book.objects.create(title='Book Two', author='Author B', publication_year=2021)

        # Hard-coded URLs for testing
        self.list_url = '/books'  # Hard-coded URL for listing books
        self.create_url = '/books/create'  # Hard-coded URL for creating a book
        self.detail_url = lambda pk: f'/books/detail/{pk}/'  # Hard-coded URL for book detail view
        self.update_url = lambda pk: f'/books/update/{pk}/'  # Hard-coded URL for updating a book
        self.delete_url = lambda pk: f'/books/delete/{pk}/'  # Hard-coded URL for deleting a book

    def test_create_book(self):
        """Test creating a new book"""
        data = {'title': 'Book Three', 'author': 'Author C', 'publication_year': 2022}
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, 'Book Three')

    def test_read_books(self):
        """Test retrieving the list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_read_book_detail(self):
        """Test retrieving a single book detail"""
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_update_book(self):
        """Test updating an existing book"""
        data = {'title': 'Updated Book One'}
        response = self.client.patch(self.update_url(self.book1.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book One')

    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(self.delete_url(self.book2.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)