from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Constants for the Post model choices
STATUS = (
    (0, "Draft"),
    (1, "Published"),
)

CATEGORY_CHOICES = [
    ('front-end-development', 'Front-End Development'),
    ('e-commerce', 'E-Commerce'),
    ('predictive-analytics', 'Predictive Analytics'),
]

class Post(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='front-end development')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name="liked_post", blank=True)
    bookmarks = models.ManyToManyField(User, related_name="bookmarked_post", blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"The title of this post is {self.title}"

    def total_likes(self):
        """
        Returns the total number of likes for the post.
        """
        return self.likes.count()

    def total_bookmarks(self):
        """
        Returns the total number of bookmarks for the post.
        """
        return self.bookmarks.count()


class Comment(models.Model):
    """
    Model representing a comment on a post.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"



class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


