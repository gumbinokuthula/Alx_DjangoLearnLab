from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

"""
This file defines views for the Book model using Django REST Framework's
generic views. Each view handles a specific CRUD operation.
"""

# List all books or create a new one
class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: Returns a list of all books
    POST: Creates a new book (requires authentication)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Read-only for unauthenticated, write for authenticated
    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


# Retrieve, update, or delete a single book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single book by ID
    PUT/PATCH: Update an existing book (requires authentication)
    DELETE: Delete a book (requires authentication)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
