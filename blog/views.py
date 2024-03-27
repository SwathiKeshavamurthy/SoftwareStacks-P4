from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
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

@login_required
def bookmarked_posts(request):
    if request.method == 'GET':
        posts = Post.objects.filter(bookmarks=request.user).order_by('-created_on')
        return render(request, 'blog/bookmarked_posts.html', {'posts': posts})

@require_POST
@login_required
def toggle_bookmark(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        if post.bookmarks.filter(id=request.user.id).exists():
            post.bookmarks.remove(request.user)
            return JsonResponse({'status': 'removed'})
        else:
            post.bookmarks.add(request.user)
            return JsonResponse({'status': 'added'})
    else:
        return redirect('some-view-name')

@login_required
def liked_posts(request):
    if request.method == 'GET':
        posts = Post.objects.filter(likes=request.user).order_by('-created_on')
        return render(request, 'blog/liked_posts.html', {'posts': posts})

@login_required
@require_POST
def toggle_like(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return JsonResponse({'liked': liked})