from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters, fields to prepopulate, and rich-text editor.
    """

    list_display = ('title', 'slug', 'author', 'category', 'status', 'approved', 'created_on', 'updated_on',)
    search_fields = ['title', 'content',]  
    list_filter = ('status', 'created_on', 'updated_on', 'author__username', 'category',) 
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

admin.site.register(Comment)
