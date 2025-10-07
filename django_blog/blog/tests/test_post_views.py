from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Post, Author  # if Author used; otherwise use User

class PostViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u1', password='pass')
        self.other = User.objects.create_user(username='u2', password='pass')
        self.post = Post.objects.create(title='T', content='C', author=self.user)

    def test_list_view(self):
        url = reverse('post-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_create_requires_login(self):
        url = reverse('post-create')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)  # redirected to login
        self.client.login(username='u1', password='pass')
        resp = self.client.post(url, {'title':'X','content':'Y'})
        self.assertIn(resp.status_code, (302, 201))  # redirect on success

    def test_update_only_author(self):
        url = reverse('post-update', args=[self.post.pk])
        self.client.login(username='u2', password='pass')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 403)  # or 302 depending on mixin behavior
