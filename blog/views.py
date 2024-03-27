from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 4


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )

def category_posts(request, category_name):
    posts = Post.objects.filter(category=category_name, status=1).order_by('-created_on')
    context = {
        'category_name': category_name,
        'posts': posts
    }
    return render(request, 'blog/category_posts.html', context)

def bookmarked_posts(request):
    # Fetch all posts that have been bookmarked by the current user
    posts = Post.objects.filter(bookmarks=request.user).order_by('-created_on')
    return render(request, 'blog/bookmarked_posts.html', {'posts': posts})

def liked_posts(request):
    # Fetch all posts that have been liked by the current user
    posts = Post.objects.filter(likes=request.user).order_by('-created_on')
    return render(request, 'blog/liked_posts.html', {'posts': posts})