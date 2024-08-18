from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.http import HttpResponseForbidden

# Helper function to check if the user is a Librarian
def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_page.html')

def handle_forbidden(request):
    return HttpResponseForbidden("You are not allowed to access this page.")