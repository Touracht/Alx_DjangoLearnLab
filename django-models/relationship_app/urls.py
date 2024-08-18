from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('listbooks/', list_books, name = 'list_books'),
    path('librarydetail/', LibraryDetailView.as_view(), name = 'library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name= "relationship_app/logout.html"), name='logout'),
    path('register/', views.register.as_view(), name = "register"),
    path('admin/', views.Admin, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]
