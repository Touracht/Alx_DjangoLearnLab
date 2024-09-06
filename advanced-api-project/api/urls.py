from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('listview/', ListView.as_view(), name = 'list_view'),
    path('detailview/', DetailView.as_view(), name = 'detail_view'),
    path('createview/', CreateView.as_view(), name = 'detail_view'),
    path('updateview/', UpdateView.as_view(), name = 'detailview'),
    path('deleteview/', DeleteView.as_view(), name = 'delete_view'),
]
