from bookshelf.models import Book

# Example: delete a book instance

book = Book.objects.get(id=1)
book.delete
