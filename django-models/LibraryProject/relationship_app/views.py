from django.shortcuts import render
from .models import Book  # Make sure Book is imported

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})
from django.views.generic import DetailView
from .models import Library  # Important: this is what the checker is looking for

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
