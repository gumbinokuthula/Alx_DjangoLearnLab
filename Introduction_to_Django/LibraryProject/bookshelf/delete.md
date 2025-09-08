from bookshelf.models import Book

# Example: delete a book by ID

Book.objects.get(id=1).delete()
