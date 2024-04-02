from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('my-bookmarks/', views.bookmarked_posts, name='bookmarked_posts'),
    path('my-likes/', views.liked_posts, name='liked_posts'),
    path('like-post/', views.like_post, name='like_post'),
    path('bookmark-post/', views.bookmark_post, name='bookmark_post'),
    path('add_post/', views.add_post, name='add_post'),
    path('my-posts/', views.user_posts, name='user_posts'),
    path('category/<slug:category_name>/', views.category_posts, name='category_posts'),
    path('commented-posts/', views.commented_posts, name='commented_posts'),
    path('search/', views.search_posts, name='search_posts'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]
