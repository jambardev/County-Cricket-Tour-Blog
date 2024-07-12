from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    # Sets number of posts on each page
    paginate_by = 6

def about_view(request):
    return render(request, 'about.html')

# Function-based view to display individual posts
def post_detail(request, slug):

    queryset = Post.objects.filter(status=1)
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

def edit_comment(request, slug, comment_id):
    post = get_object_or_404(Post, slug=slug, status=1)
    comment = get_object_or_404(Comment, pk=comment_id, post=post)
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid():
            comment_form.save()
            messages.add_message(request, messages.SUCCESS, 'Thanks, Comment Updated!')
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        else:
            messages.add_message(request, messages.ERROR, 'Sorry, Error updating comment!')

    else:
        comment_form = CommentForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {'form': comment_form, 'post': post})