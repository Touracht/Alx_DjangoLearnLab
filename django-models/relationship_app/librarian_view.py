from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .role_checks import is_librarian  # assuming role_checks.py contains your role checking functions

@user_passes_test(is_librarian)
def librarian_view(request):
    # Your logic for librarian view
    return render(request, 'librarian_template.html')  # replace with your template