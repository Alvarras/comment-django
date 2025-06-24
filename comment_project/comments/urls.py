from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # URL baru untuk halaman tambah post
    path('post/add/', views.add_post, name='add_post'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:post_pk>/comment/<int:comment_pk>/edit/', views.edit_comment, name='edit_comment'),
    path('post/<int:post_pk>/comment/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
]