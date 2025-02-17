from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'

class PostPage(TemplateView):
    template_name = 'post.html'

class LoginPage(TemplateView):
    template_name = 'login.html'

class FeedPage(TemplateView):
    template_name = 'feed.html'