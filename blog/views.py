from django.http import (
    JsonResponse, Http404, HttpResponseRedirect, HttpResponseForbidden
)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.db.models import Q
from django.db import IntegrityError


class PostList(generic.ListView):
    """
    View for displaying a list of published posts.
    """
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 4


def post_detail(request, slug):
    """
    View for displaying the details of a specific post and handling comments.
    """
    post = get_object_or_404(Post, slug=slug)
    if post.status != 1 and post.author != request.user:
        raise Http404("Post not found or not published")
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    likes_count = post.likes.count()
    bookmarks_count = post.bookmarks.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    else:
        comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "likes_count": likes_count, 
            "bookmarks_count": bookmarks_count, 
            "comment_form": comment_form,
        },
    )


def category_posts(request, category_name):
    """
    View for displaying posts filtered by category.
    """
    posts = Post.objects.filter(category=category_name, status=1).order_by('-created_on')
    context = {
        'category_name': category_name,
        'posts': posts
    }
    return render(request, 'blog/category_posts.html', context)


@login_required
def bookmarked_posts(request):
    """
    View for displaying the user's bookmarked posts.
    """
    if request.method == 'GET':
        posts = Post.objects.filter(bookmarks=request.user).order_by('-created_on')
        return render(request, 'blog/bookmarked_posts.html', {'posts': posts})


@login_required
def liked_posts(request):
    """
    View for displaying the user's liked posts.
    """
    if request.method == 'GET':
        posts = Post.objects.filter(likes=request.user).order_by('-created_on')
        return render(request, 'blog/liked_posts.html', {'posts': posts})


@login_required
def user_posts(request):
    """
    View for displaying posts authored by the current user.
    """
    if request.method == 'GET':
        posts = Post.objects.filter(author=request.user).order_by('-created_on')
        return render(request, 'blog/user_posts.html', {'posts': posts})


@login_required
def like_post(request):
    """
    View for handling post likes.
    """
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        liked = False
        message = 'Post unliked.'
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
            liked = True
            message = 'Post liked.'
        return JsonResponse({'liked': liked, 'likes_count': post.likes.count(), 'message': message})
    else:
        return JsonResponse({'error': 'Invalid request method'})


@login_required
def bookmark_post(request):
    """
    View for handling post bookmarks.
    """
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        bookmarked = False
        message = 'Post bookmark removed.'
        if request.user in post.bookmarks.all():
            post.bookmarks.remove(request.user)
        else:
            post.bookmarks.add(request.user)
            bookmarked = True
            message = 'Post bookmarked.'
        return JsonResponse({'bookmarked': bookmarked, 'bookmarks_count': post.bookmarks.count(), 'message': message})
    else:
        return JsonResponse({'error': 'Invalid request method'})


@login_required
def commented_posts(request):
    """
    View for displaying posts commented on by the current user.
    """
    if request.method == 'GET':
        commented_post_ids = Comment.objects.filter(author=request.user).values_list('post_id', flat=True)
        posts = Post.objects.filter(id__in=commented_post_ids).order_by('-created_on')
        return render(request, 'blog/commented_posts.html', {'posts': posts})


def comment_edit(request, slug, comment_id):
    """
    View for editing comments.
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View for deleting comments.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def search_posts(request):
    """
    View for searching posts.
    """
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query),
            status=1
        ).distinct()
    else:
        posts = Post.objects.none()  # Return an empty QuerySet if no query is specified

    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})


@login_required
def add_post(request):
    """
    View for adding new posts.
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.success(request, 'Post added successfully and is awaiting approval.')
            return redirect('home')  # Redirect to a relevant page
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})


@login_required
def edit_post(request, slug):
    """
    View for editing existing posts.
    """
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if post.approved:
        messages.error(request, "Approved posts cannot be edited.")
        return redirect('post_detail', slug=slug)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post successfully updated.')
            return redirect('post_detail', slug=slug)
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'edit_mode': True,
        'post': post
    }
    return render(request, 'blog/add_post.html', context)


@login_required
def delete_post(request, slug):
    """
    View for deleting existing posts.
    """
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if not post.approved:
        post.delete()
        messages.success(request, "Post successfully deleted.")
    else:
        messages.error(request, "Approved posts cannot be deleted.")
    return redirect('user_posts')  # Redirect to the view showing the user's posts
