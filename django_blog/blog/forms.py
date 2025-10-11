from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post
from .models import Comment
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # <--- include "tags"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
            'tags': TagWidget(),  # <--- ensures "TagWidget()" string exists
        }

class CustomUserCreationForm(UserCreationForm):
    """
    Extends Django's UserCreationForm to include email.
    """
    email = forms.EmailField(required=True, help_text="Enter a valid email address")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserProfileForm(forms.ModelForm):
    """
    Simple form to edit User fields (username, email).
    """
    class Meta:
        model = User
        fields = ("username", "email")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'}),
        }
def clean_content(self):
        content = self.cleaned_data.get("content")
        if not content or len(content.strip()) < 2:
            raise forms.ValidationError("Comment cannot be empty or too short.")
        return content