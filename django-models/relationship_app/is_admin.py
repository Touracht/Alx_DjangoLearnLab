from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def is_admin(request):
    return render(request, 'relationship_app/admin_view.html')