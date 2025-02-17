from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('post/', views.PostPage.as_view(), name='post'),
    path('login/', views.LoginPage.as_view(), name='login'),
    path('feed/', views.FeedPage.as_view(), name='feed'),
]
