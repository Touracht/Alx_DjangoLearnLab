from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .role_checks import is_admin  # assuming role_checks.py contains your role checking functions

@user_passes_test(is_admin)
def admin_view(request):
    # Your logic for admin view
    return render(request, 'admin_template.html')  # replace with your template