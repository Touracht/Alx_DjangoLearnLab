from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .role_checks import is_member  # assuming role_checks.py contains your role checking functions

@user_passes_test(is_member)
def member_view(request):
    # Your logic for member view
    return render(request, 'member_template.html')  # replace with your template