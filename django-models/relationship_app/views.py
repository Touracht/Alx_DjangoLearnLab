from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login

def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request,'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

class register(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

# myapp/views.py
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile

# Helper function to check if the user is an Admin
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'admin'

@user_passes_test(is_admin)
def Admin(request):
    # Logic for the admin view
    return render(request, 'admin_page.html')

from django.conf.urls import handler403
from .views import handle_forbidden

handler403 = handle_forbidden





