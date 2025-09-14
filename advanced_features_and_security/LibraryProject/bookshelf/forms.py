from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """
    ExampleForm for adding/editing Book objects.
    """
    class Meta:
        model = Book
        fields = ['title', 'author']
