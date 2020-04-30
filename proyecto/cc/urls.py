from django.urls import path, include
from .views import OnePost, HomePageView, CreatePostView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.About.as_view(), name='about'),
    path('<int:post_id>', OnePost.as_view(), name='onePost'),
    path('addPost/', CreatePostView.as_view(), name='add'),
    path('list/', HomePageView.as_view(), name='list'),
]
