from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm

def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'comments/home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-date_posted')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'comments/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })