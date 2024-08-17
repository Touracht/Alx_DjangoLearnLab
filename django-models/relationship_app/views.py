from django.shortcuts import render
from . import models
from django.views.generic import DetailView

def list_books(request):
    books = models.Book.objects.all()
    context = {'books': books}
    return render(request,'list_books.html', context)

class library_detail(DetailView):
    model = models.Library
    template_name = 'library_detail.html'


