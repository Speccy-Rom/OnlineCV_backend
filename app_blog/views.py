from django.shortcuts import render
from django.views.generic import ListView, DetailView

from app_blog.models import Blog, Category


class BlogByCategory(ListView):
    model = Blog
    template_name = 'index.html'
    context_object_name = 'cat_posts'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogByCategory, self).get_context_data()
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])

    def get_queryset(self):
        return Blog.objects.filter(slug=self.kwargs['slug'])


class HomeBlog(ListView):
    model = Blog
    template_name = 'index.html'
    context_object_name = 'posts'

    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeBlog, self).get_context_data()
        context['title'] = 'Home'
        return context

    # def get_queryset(self):
    #     return Portfolio.objects.all()[0:3]


class ViewPosts(DetailView):
    model = Blog
    template_name = 'app_blog/page-blog-detail.html'
    context_object_name = 'detail_post'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ViewPosts).get_context_data()
        context['title'] = Blog.objects.get(slug=self.kwargs['slug'])

    def get_queryset(self):
        return Blog.objects.filter(slug=self.kwargs['slug'])
