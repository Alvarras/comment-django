from django.shortcuts import render, get_object_or_404, redirect
# Import decorator untuk memastikan user sudah login
from django.contrib.auth.decorators import login_required
from .models import Post
# Import form yang baru kita buat
from .forms import CommentForm, PostForm

def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'comments/home.html', {'posts': posts})

# View baru untuk menambah post
@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Simpan form tapi jangan langsung ke database
            post = form.save(commit=False)
            # Set author dari user yang sedang login
            post.author = request.user
            post.save()
            # Arahkan kembali ke halaman utama
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'comments/add_post.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-date_posted')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user # Pastikan user sudah login untuk berkomentar
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'comments/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect('home')
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'comments/add_post.html', {'form': form, 'edit': True})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user:
        post.delete()
    return redirect('home')

@login_required
def edit_comment(request, post_pk, comment_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment = get_object_or_404(post.comments, pk=comment_pk)
    if comment.user != request.user:
        return redirect('post_detail', pk=post.pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comments/edit_comment.html', {'form': form, 'post': post, 'comment': comment})

@login_required
def delete_comment(request, post_pk, comment_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment = get_object_or_404(post.comments, pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
    return redirect('post_detail', pk=post.pk)