from django.urls import path
from . import views

urlpatterns = [
    path('listbooks/',views.list_books, name = 'list_books'),
    path('librarydetail/', views.library_detail.as_view(), name = 'library_detail')
]
