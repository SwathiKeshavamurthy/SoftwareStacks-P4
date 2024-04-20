from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post, Comment
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied

class BlogFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser2', password='54321')
        self.client.login(username='testuser2', password='54321')
        self.post = Post.objects.create(
            title='Another Test Post',
            content='More test content here',
            author=self.user,
            status=1
        )
        self.comment_form_data = {
            'body': 'A test comment',
            'post': self.post.id,
            'author': self.user.id
        }

    def test_comment_submission(self):
        """
        Test submitting a valid comment through the post detail view.
        """
        response = self.client.post(reverse('post_detail', args=[self.post.slug]), {
            'body': 'A test comment'
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful form submission

    def test_delete_post_permission(self):
        """
        Test that the delete post view only allows the post owner to delete the post.
        """
        # Ensure the correct user is logged in
        self.client.login(username='testuser2', password='54321')
        response = self.client.post(reverse('delete_post', args=[self.post.slug]))
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion

    def test_search_posts(self):
        """
        Test the search functionality to ensure it returns correct results.
        """
        response = self.client.get(reverse('search_posts'), {'q': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Another Test Post')


class BlogViewsTests(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.client.login(username='testuser', password='12345')

        # Create a post
        self.post = Post.objects.create(
            title='A Test Post',
            content='Just some test content',
            author=self.user,
            status=1
        )

    def test_post_detail_view(self):
        """
        Test the post detail view to ensure it returns a 200 response and uses the correct template.
        """
        response = self.client.get(reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_like_post_view(self):
        """
        Test the like post view to ensure it handles the request correctly when a user likes a post.
        """
        post_id = self.post.id
        response = self.client.post(reverse('like_post'), {'post_id': post_id})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['liked'])

    def test_unauthenticated_access(self):
        """
        Test that unauthenticated users are redirected when trying to access restricted views.
        """
        self.client.logout()
        response = self.client.get(reverse('like_post'))
        self.assertNotEqual(response.status_code, 200)
        self.assertTrue(response.status_code, 302)  # Redirect to login

class LikeAndBookmarkTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.client.login(username='testuser', password='12345')
        self.post = Post.objects.create(
            title="Sample Post",
            content="Just a test post.",
            author=self.user,
            status=1
        )

    def test_like_post(self):
        """
        Test the like functionality for a post.
        """
        url = reverse('like_post')
        response = self.client.post(url, {'post_id': self.post.id})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'liked': True, 'likes_count': 1, 'message': 'Post liked.'})

    def test_unlike_post(self):
        """
        Test the unlike functionality after liking a post.
        """
        # First, like the post
        self.client.post(reverse('like_post'), {'post_id': self.post.id})
        # Then, unlike it
        response = self.client.post(reverse('like_post'), {'post_id': self.post.id})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'liked': False, 'likes_count': 0, 'message': 'Post unliked.'})

    def test_bookmark_post(self):
        """
        Test the bookmark functionality for a post.
        """
        url = reverse('bookmark_post')
        response = self.client.post(url, {'post_id': self.post.id})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'bookmarked': True, 'bookmarks_count': 1, 'message': 'Post bookmarked.'})

    def test_unbookmark_post(self):
        """
        Test the unbookmark functionality after bookmarking a post.
        """
        # First, bookmark the post
        self.client.post(reverse('bookmark_post'), {'post_id': self.post.id})
        # Then, unbookmark it
        response = self.client.post(reverse('bookmark_post'), {'post_id': self.post.id})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'bookmarked': False, 'bookmarks_count': 0, 'message': 'Post bookmark removed.'})
