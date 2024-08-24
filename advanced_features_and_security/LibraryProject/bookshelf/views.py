from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

@permission_required('bookshelf.can_view', raise_exception = True)
def create_book(request):
    if request == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm

@permission_required('bookshelf.can_edit', raise_exception = True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk = pk)
    if request == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid:
            form.save()
            return redirect('book_detail', pk = book.pk)

    else:
        form = BookForm(instance=book)

@permission_required('bookshelf.can_delete', raise_exception = True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk = pk)
    if request == 'POST':
        book.delete()
        return redirect('book_list')

from .forms import ExampleForm


    
