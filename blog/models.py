from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


class Post(models.Model):
    """
    Model representing a blog post.
    """

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

    REVIEW_STATUS = (
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
    )

    # Fields for the Post model
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES,
                                default='front-end development')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=False)
    post_review_status = models.CharField(max_length=10, choices=REVIEW_STATUS,
                                          default='pending')
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name="liked_post", blank=True)
    bookmarks = models.ManyToManyField(User, related_name="bookmarked_post",
                                       blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"The title of this post is {self.title}"

    def likes_count(self):
        """
        Returns the total number of likes for the post.
        """
        return self.likes.count()

    def bookmarks_count(self):
        """
        Returns the total number of bookmarks for the post.
        """
        return self.bookmarks.count()

    def save(self, *args, **kwargs):
        """
        Overrides the save method to generate a unique slug.
        """
        # If the instance doesn't have a slug or the title has changed
        # and the slug is based on the title
        if not self.slug or slugify(self.title) != self.slug:
            self.slug = original_slug = slugify(self.title)
            # Ensure the slug is unique
            for x in range(1, 100):  # Arbitrary limit to prevent infinite loop
                if not Post.objects.filter(slug=self.slug).exists():
                    break
                self.slug = f'{original_slug}-{x}'
            else:
                # As a last resort, append the length of posts
                # to ensure uniqueness
                self.slug = (
                 f'{original_slug}-'
                 f'{Post.objects.annotate(text_len=Length("title")).count()}'
                )
        super(Post, self).save(*args, **kwargs)


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
    """
    Model representing a category.
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        """
        Overrides the save method to generate a unique slug.
        """
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
