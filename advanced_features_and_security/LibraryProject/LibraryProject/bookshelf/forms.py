# LibraryProject/bookshelf/forms.py
from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """
    ExampleForm (ModelForm) used by the form_example view.
    Uses Book model fields title and author.
    """
    class Meta:
        model = Book
        fields = ['title', 'author']
