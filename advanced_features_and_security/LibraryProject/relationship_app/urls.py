from django.urls import path
from . import views

urlpatterns = [
    # Add book
    path('add_book/', views.add_book, name='add_book'),

    # Edit book
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),

    # Delete book
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]
