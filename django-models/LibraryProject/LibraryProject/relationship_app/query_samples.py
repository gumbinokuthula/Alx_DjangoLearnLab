from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)

# List all books in a library
def books_in_library(library_name):
    return Library.objects.get(name=library_name).books.all()

# Retrieve the librarian for a library
def get_librarian(library_name):
    return Library.objects.get(name=library_name).librarian
