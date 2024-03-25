from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters, fields to prepopulate, and rich-text editor.
    """

    list_display = ('title', 'slug', 'author', 'status', 'created_on', 'updated_on',)
    search_fields = ['title', 'author__username']  # Added 'author__username' for searching by author's username
    list_filter = ('status', 'created_on', 'updated_on', 'author__username',)  # Added 'author__username' for filtering by author's username
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

admin.site.register(Comment)
