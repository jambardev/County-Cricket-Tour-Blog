from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import PostForm
from .forms import CommentForm


# Create your views here.

# View for the home page
class PostList(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = "blog/index.html"
    # Sets number of posts on each page
    paginate_by = 6


def about_view(request):
    return render(request, 'about.html')


# View for a user to add a new post
@login_required
def add_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(
                request,
                'Thanks for joining the discussion, post created successfully.'
            )
            return redirect('home')
        else:
            messages.error(request, 'Error creating post.')
    else:
        form = PostForm()

    return render(request, 'blog/add_post.html', {'form': form})


# Function-based view to display individual posts
def post_detail(request, slug):

    queryset = Post.objects
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-added_on")
    comment_count = post.comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted, thanks for joining the discussion.'
            )
    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }
    )


# View allowing a user to edit their own comments
@login_required
def edit_comment(request, slug, comment_id):
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id, post=post)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid():
            comment.author = request.user
            comment_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Thanks, Comment Updated!'
            )
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Sorry, Error updating comment! You can only update your own comments.'
            )

    else:
        comment_form = CommentForm(instance=comment)

    return render(
        request,
        'blog/edit_comment.html',
        {'form': comment_form, 'post': post}
    )


# View allowing a user to delete their own comments
@login_required
def delete_comment(request, slug, comment_id):
    queryset = Post.objects
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'No problem, comment deleted!'
        )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'You can only delete your own comments!'
        )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# View allowing a user to delete their own posts
@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.author == request.user:
        if request.method == "POST":
            post.delete()
            messages.add_message(
                request,
                messages.SUCCESS,
                'No problem, that post has been deleted!'
            )
            return HttpResponseRedirect(reverse('home'))
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'You can only delete your own posts!'
        )

    return render(request, 'blog/delete_post.html', {'post': post})
