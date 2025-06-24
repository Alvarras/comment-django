from django import forms
# Import Post model
from .models import Comment, Post, User

# Form untuk menambah Post baru
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        # id dan date_posted tidak perlu diinput user

# Form untuk menambah komentar (sudah ada)
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Write your comment here...'
        })
    )

    class Meta:
        model = Comment
        fields = ['content']
        # id, post, user, date_posted tidak perlu diinput user