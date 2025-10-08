from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Post

class TagSearchTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u', password='p')
        self.p1 = Post.objects.create(title='Django tips', content='use django', author=self.user)
        self.p2 = Post.objects.create(title='Python', content='python code', author=self.user)
        # add tags
        self.p1.tags.add('django', 'web')
        self.p2.tags.add('python')

    def test_tag_filter(self):
        url = reverse('posts-by-tag', kwargs={'tag_name': 'django'})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Django tips')
        self.assertNotContains(resp, 'Python')

    def test_search_by_title(self):
        url = reverse('post-search') + '?q=Python'
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Python')

    def test_search_by_tag(self):
        url = reverse('post-search') + '?q=django'
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Django tips')
