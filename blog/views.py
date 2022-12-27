from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import BlogPost


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog.html'
