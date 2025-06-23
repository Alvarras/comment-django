from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # URL baru untuk halaman tambah post
    path('post/add/', views.add_post, name='add_post'),
]