from . import views
from django.urls import path
from .views import category_posts, bookmarked_posts

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_name>/', category_posts, name='category_posts'),
    path('my-bookmarks/', bookmarked_posts, name='bookmarked_posts'),
]