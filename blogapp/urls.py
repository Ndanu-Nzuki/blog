
from django.urls import path
from .views import (
	PostListView, 
	PostDetailView,
	PostCreateView,
	PostUpdateView,
  PostDeleteView,
  UserPostListView

	)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
    path('post/new', PostCreateView.as_view(), name = 'post-create'),
   	path('post/<pk>/', PostDetailView.as_view(), name = 'post-detail'),
   	path('post/<pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
   	path('post/<pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('about/', views.about, name = 'blog-about'),
    path('contact/', views.contact, name = 'blog-contact')
]