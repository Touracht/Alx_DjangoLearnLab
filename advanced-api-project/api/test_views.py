from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from .models import Book

class BookModelTestCase(TestCase):
    def setUp(self):
        # Initialize the API client
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create some sample books
        self.book1 = Book.objects.create(title='Book One', author='Author A', publication_year=2020)
        self.book2 = Book.objects.create(title='Book Two', author='Author B', publication_year=2021)

        # Define URLs for testing
        self.list_url = '/books'  
        self.create_url = '/books/create'  
        self.detail_url = lambda pk: f'/books/detail/{pk}/'  
        self.update_url = lambda pk: f'/books/update/{pk}/'  
        self.delete_url = lambda pk: f'/books/delete/{pk}/'  

    def test_create_book_authenticated(self):
        """Test creating a new book with an authenticated user"""
        # Log in the test user
        self.client.login(username='testuser', password='testpass')

        # Data for the new book
        data = {'title': 'Book Three', 'author': 'Author C', 'publication_year': 2022}

        # Make a POST request to create a book
        response = self.client.post(self.create_url, data, format='json')

        # Check that the response status is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)  # Verify a new book was added

    def test_create_book_unauthenticated(self):
        """Test that an unauthenticated user cannot create a new book"""
        # Data for the new book
        data = {'title': 'Book Four', 'author': 'Author D', 'publication_year': 2023}

        # Make a POST request to create a book without logging in
        response = self.client.post(self.create_url, data, format='json')

        # Check that the response status is 403 (Forbidden) or 401 (Unauthorized)
        self.assertIn(response.status_code, [status.HTTP_403_FORBIDDEN, status.HTTP_401_UNAUTHORIZED])

    def test_read_books_authenticated(self):
        """Test retrieving the list of books with an authenticated user"""
        # Log in the test user
        self.client.login(username='testuser', password='testpass')

        # Make a GET request to retrieve the list of books
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Verify the number of books

    def test_read_book_detail_authenticated(self):
        """Test retrieving a single book detail with an authenticated user"""
        # Log in the test user
        self.client.login(username='testuser', password='testpass')

        # Make a GET request to retrieve the book detail
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_update_book_authenticated(self):
        """Test updating an existing book with an authenticated user"""
        # Log in the test user
        self.client.login(username='testuser', password='testpass')

        # Data for updating the book
        data = {'title': 'Updated Book One'}

        # Make a PATCH request to update the book
        response = self.client.patch(self.update_url(self.book1.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book One')

    def test_delete_book_authenticated(self):
        """Test deleting a book with an authenticated user"""
        # Log in the test user
        self.client.login(username='testuser', password='testpass')

        # Make a DELETE request to delete the book
        response = self.client.delete(self.delete_url(self.book2.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)  # Verify the book was deleted