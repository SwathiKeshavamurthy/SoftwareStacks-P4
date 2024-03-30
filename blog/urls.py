from django.urls import path
from . import views
from .views import (
    category_posts,
    bookmarked_posts,
    liked_posts,
    commented_posts,
    search_posts,
)

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('my-bookmarks/', bookmarked_posts, name='bookmarked_posts'),
    path('my-likes/', liked_posts, name='liked_posts'),
    path('category/<slug:category_name>/', category_posts, name='category_posts'),
    path('commented-posts/', commented_posts, name='commented_posts'),
    path('search/', search_posts, name='search_posts'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]
