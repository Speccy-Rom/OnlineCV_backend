from django.shortcuts import render
from django.views import View

from .models import Blog


class BlogView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        posts = Blog.objects.all()
        context['posts'] = posts
        return render(request, 'app_blog/page-blog.html', context)

