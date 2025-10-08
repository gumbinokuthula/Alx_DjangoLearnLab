# blog/urls.py
from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    create_comment, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comments:
    path('post/<int:post_id>/comments/new/', create_comment, name='comment-create'),
    path('post/<int:post_id>/comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('post/<int:post_id>/comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
