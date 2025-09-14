# LibraryProject/bookshelf/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import ExampleForm  # <--- required by checker

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def form_example(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
