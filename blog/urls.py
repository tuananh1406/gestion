from django.urls import path
from .views import(
    PostListView,
    PostCreateView,
    UserPostListView
)
urlpatterns = [
    path('/home', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    
]


