from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, PostForm, CustomUserUpdateForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserProfileForm, CommentForm
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import UserProfile
from django.urls import reverse

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.email = form.cleaned_data.get('email')
            user.save()
            return redirect('login')
    
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

@login_required
def profile_management(request):
    if request.method == 'POST':
        user_form = CustomUserUpdateForm(request.POST, instance=request.user)
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile_form = UserProfileForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('home')
    else:
        user_form = CustomUserUpdateForm(instance=request.user)
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile_form = UserProfileForm(instance=profile)

    return render(request, 'blog/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


class HomePageView(TemplateView):
    template_name = 'blog/home.html'
    
# The following are Post related Views

# blog/views.py

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.select_related('post', 'author').all()
        context['form'] = CommentForm() 
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)        

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm(user=self.request.user)  # Pass the user to the form
        context['comments'] = self.object.comments.all()  # Fetch comments related to the post
        return context

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    post_form = PostForm
    fields = ['title', 'content']
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts') 

    def get(self, request, *args, **kwargs):
        
        self.object = self.get_object()
        if self.object.author != self.request.user:
            
            return self.handle_no_permission()
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        """Handle the post request to delete the post."""
        self.object = self.get_object()
        if self.object.author != self.request.user:

            return self.handle_no_permission()
        return super().post(request, *args, **kwargs)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

#The following are comment related views.

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def get_form_kwargs(self):
        """Pass the user to the form."""
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the user to the form
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})

