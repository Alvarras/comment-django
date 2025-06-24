from rest_framework import viewsets, permissions
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    id = serializers.UUIDField(read_only=True)
    date_posted = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'date_posted', 'author']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    id = serializers.UUIDField(read_only=True)
    date_posted = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content', 'date_posted']

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    def perform_update(self, serializer):
        if self.request.user != self.get_object().author:
            raise serializers.ValidationError('You can only edit your own posts.')
        serializer.save()
    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise serializers.ValidationError('You can only delete your own posts.')
        instance.delete()

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-date_posted')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def perform_update(self, serializer):
        if self.request.user != self.get_object().user:
            raise serializers.ValidationError('You can only edit your own comments.')
        serializer.save()
    def perform_destroy(self, instance):
        if self.request.user != instance.user:
            raise serializers.ValidationError('You can only delete your own comments.')
        instance.delete() 