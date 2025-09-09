from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in list view
    list_filter = ('publication_year', 'author')            # Filters in sidebar
    search_fields = ('title', 'author')                     # Search box functionality

admin.site.register(Book, BookAdmin)
