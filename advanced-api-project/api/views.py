from django_filters import rest_framework as filters  # ✅ exact import for filtering
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

"""
ListView now supports:
- Filtering by title, author, and publication_year
- Searching by title and author
- Ordering by title and publication_year
"""

class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # ✅ Add filter/search/order backends
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # ✅ Filtering fields
    filterset_fields = ["title", "author__name", "publication_year"]

    # ✅ Search fields
    search_fields = ["title", "author__name"]

    # ✅ Ordering fields
    ordering_fields = ["title", "publication_year"]

    # Default ordering
    ordering = ["title"]
