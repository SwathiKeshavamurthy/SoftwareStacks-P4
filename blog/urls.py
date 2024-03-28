from . import views
from django.urls import path
from .views import category_posts, bookmarked_posts, liked_posts, commented_posts
from .views import toggle_bookmark, toggle_like

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('my-bookmarks/', bookmarked_posts, name='bookmarked_posts'),
    path('toggle-bookmark/', views.toggle_bookmark, name='toggle_bookmark'),
    path('my-likes/', liked_posts, name='liked_posts'),
    path('toggle-like/', views.toggle_like, name='toggle_like'),
    path('category/<slug:category_name>/', category_posts, name='category_posts'),
    path('commented-posts/', views.commented_posts, name='commented_posts'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
]
    
    