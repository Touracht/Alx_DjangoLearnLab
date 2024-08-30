from django.urls import path
from .models import BookList

urlpatterns = [
    path("booklist/", BookList.as_view(),name = 'book_list')
]
