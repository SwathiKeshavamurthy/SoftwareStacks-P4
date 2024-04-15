from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register the Post model with customizations.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters, fields to prepopulate, and rich-text editor.
    """

    list_display = ('title', 'slug', 'author', 'category',
                    'status', 'approved', 'created_on', 'updated_on',)
    search_fields = ['title', 'content', ]
    list_filter = ('status', 'approved', 'created_on',
                   'updated_on', 'author__username', 'category',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register the Comment model with customizations.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Customize the admin list view for Comment model to include
    display of post, author, and approval status.
    """
    list_display = ('post', 'author', 'approved', 'created_on',)
    list_filter = ('approved', 'created_on', 'author')
    search_fields = ('body', 'author__username', 'post__title',)
