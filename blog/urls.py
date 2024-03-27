from . import views
from django.urls import path
from .views import category_posts, bookmarked_posts, liked_posts

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('my-bookmarks/', bookmarked_posts, name='bookmarked_posts'),
    path('my-likes/', liked_posts, name='liked_posts'),
    path('category/<slug:category_name>/', category_posts, name='category_posts'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
    