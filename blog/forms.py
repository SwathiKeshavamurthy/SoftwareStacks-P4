from .models import Comment, Post
from django import forms


# Define a form for creating and updating comments.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# Define a form for creating and updating posts.
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'featured_image', 'content', 'category', 'excerpt']
