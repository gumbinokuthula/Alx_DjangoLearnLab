# bookshelf/views.py
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm  # we’ll make this form next


def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


def form_example(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
