from . import views
from .views import *
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.About.as_view(), name='about'),
    path('<int:post_id>', OnePost.as_view(), name='onePost'),
    path('addPost/', CreatePostView.as_view(), name='add'),
    path('list/', HomePageView.as_view(), name='list'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
]
