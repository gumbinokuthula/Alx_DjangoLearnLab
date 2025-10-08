# blog/tests/test_comments.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Post, Comment

class CommentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='pass')
        self.other = User.objects.create_user(username='user2', password='pass')
        self.post = Post.objects.create(title='T', content='C', author=self.user)

    def test_create_comment_authenticated(self):
        self.client.login(username='user2', password='pass')
        url = reverse('comment-create', args=[self.post.pk])
        resp = self.client.post(url, {'content': 'Nice post!'}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.post.comments.count(), 1)
        comment = self.post.comments.first()
        self.assertEqual(comment.author, self.other)

    def test_create_comment_unauthenticated_redirects(self):
        url = reverse('comment-create', args=[self.post.pk])
        resp = self.client.post(url, {'content': 'Hi'}, follow=True)
        # unauthenticated users should be redirected to login
        self.assertTrue(resp.redirect_chain)
    
    def test_edit_comment_only_author(self):
        comment = Comment.objects.create(post=self.post, author=self.user, content='A')
        url = reverse('comment-update', args=[self.post.pk, comment.pk])
        # other user cannot edit
        self.client.login(username='user2', password='pass')
        resp = self.client.get(url)
        # Should be forbidden or redirect — ensure not 200
        self.assertNotEqual(resp.status_code, 200)
        # author can edit
        self.client.login(username='user1', password='pass')
        resp2 = self.client.post(url, {'content': 'Updated'}, follow=True)
        self.assertEqual(resp2.status_code, 200)
        comment.refresh_from_db()
        self.assertEqual(comment.content, 'Updated')

    def test_delete_comment_only_author(self):
        comment = Comment.objects.create(post=self.post, author=self.user, content='A')
        url = reverse('comment-delete', args=[self.post.pk, comment.pk])
        # other user cannot delete
        self.client.login(username='user2', password='pass')
        resp = self.client.post(url)
        self.assertNotEqual(resp.status_code, 302)  # should not redirect to success
        # author can delete
        self.client.login(username='user1', password='pass')
        resp2 = self.client.post(url, follow=True)
        self.assertEqual(resp2.status_code, 200)
        self.assertEqual(self.post.comments.count(), 0)
