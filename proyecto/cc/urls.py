from . import views
from .views import OnePost, HomePageView, CreatePostView
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.About.as_view(), name='about'),
    path('<int:post_id>', OnePost.as_view(), name='onePost'),
    path('addPost/', CreatePostView.as_view(), name='add'),
    path('list/', HomePageView.as_view(), name='list'),
    # path('', include('posts.urls')),
]
