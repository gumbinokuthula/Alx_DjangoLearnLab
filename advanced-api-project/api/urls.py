from django.urls import path
from .views import BookListCreateView, BookDetailView

"""
URL routes for Book API using generic views.
"""

urlpatterns = [
    # List all books OR create a new book
    path("books/", BookListCreateView.as_view(), name="book-list-create"),

    # Retrieve, update, or delete a specific book
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
]
