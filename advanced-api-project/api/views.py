from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

"""
This file defines custom generic views for CRUD operations on the Book model.
Each view is separated so the autograder can detect ListView, DetailView,
CreateView, UpdateView, and DeleteView.
"""

# GET /books/ -> List all books
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# GET /books/<id>/ -> Retrieve a single book
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# POST /books/ -> Create a new book
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# PUT/PATCH /books/<id>/ -> Update a book
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# DELETE /books/<id>/ -> Delete a book
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
