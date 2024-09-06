from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('books', ListView.as_view(), name = 'list_view'),
    path('books/detail/<int:pk>/', DetailView.as_view(), name = 'detail_view'),
    path('books/create', CreateView.as_view(), name = 'detail_view'),
    path('books/update/<int:pk>/', UpdateView.as_view(), name = 'detailview'),
    path('books/delete/<int:pk>/', DeleteView.as_view(), name = 'delete_view'),
]
