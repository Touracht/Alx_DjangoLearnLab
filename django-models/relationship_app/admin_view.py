from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.http import HttpResponseForbidden

def Admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'admin'

@user_passes_test(Admin)
def admin_view(request):
    return render(request, 'admin_page.html')

def handle_forbidden(request):
    return HttpResponseForbidden("You are not allowed to access this page.")