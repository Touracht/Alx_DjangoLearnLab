from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserProfileForm
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from django.urls import reverse_lazy

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm()
        if form.is_valid():
            user = form.save(commit = False)
            user.email = form.cleaned_data.get('email')
            user.save()
            return redirect('login')
    
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'from': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

@login_required()
def profile_management(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, instance = request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():user_form.save() 
        profile_form.save()

        return redirect('home')
    
    else:
        user_form = CustomUserCreationForm(instance = request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'blog/profile.html', {'user_form':user_form, 'profile_form': profile_form})

class LogOut(LogoutView):
    template_name = 'blog/logout.html'
    successful_url = reverse_lazy('home')

class HomePageView(TemplateView):
    template_name = 'blog/home.html'
    



  







