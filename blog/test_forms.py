from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import CommentForm, PostForm

class CommentFormTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(
            title='A Valid Post Title',
            content='Some valid content here.',
            author=self.user,
            status=1,
            excerpt='A valid excerpt'
        )

    def test_comment_form_valid(self):
        """
        Test that the CommentForm is valid with proper data.
        """
        form_data = {'body': 'A valid comment'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid(self):
        """
        Test that the CommentForm is invalid when no data is provided.
        """
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors)

class PostFormTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_post_form_valid(self):
        """
        Test the PostForm with all required fields filled correctly.
        """
        form_data = {
            'title': 'Unique Title',
            'content': 'Some content here.',
            'category': 'front-end-development',
            'excerpt': 'A valid excerpt'
        }
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_post_form_invalid(self):
        """
        Test the PostForm with missing required fields.
        """
        form_data = {
            'title': '',  # missing title
            'content': 'Some content here.'
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('category', form.errors)
        self.assertIn('excerpt', form.errors)

