from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.http import HttpResponse

@permission_required("relationship_app.can_add_book")
def add_book(request):
    # placeholder logic (later could use forms)
    return HttpResponse("You are allowed to add a book!")

@permission_required("relationship_app.can_change_book")
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return HttpResponse(f"You are allowed to edit the book: {book.title}")

@permission_required("relationship_app.can_delete_book")
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return HttpResponse(f"You are allowed to delete the book: {book.title}")
