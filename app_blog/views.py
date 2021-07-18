from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from taggit.models import Tag

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
    template_name = 'app_blog/page-blog.html'
    context_object_name = 'posts'

    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeBlog, self).get_context_data()
        context['title'] = 'Blog'
        return context

    # def get_queryset(self):
    #     return Portfolio.objects.all()[0:3]


class ViewPosts(DetailView):
    model = Blog
    template_name = 'app_blog/page-blog-detail.html'
    context_object_name = 'detail_post'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ViewPosts, self).get_context_data()
        context['title'] = Blog.objects.get(slug=self.kwargs['slug'])

    def get_queryset(self):
        return Blog.objects.filter(slug=self.kwargs['slug'])


class TagView(View):
    def get(self, request, slug, *args, **kwargs):
        tag = get_object_or_404(Tag, slug=slug)
        posts = Blog.objects.filter(tag=tag)
        common_tags = Blog.tag.most_common()
        return render(request, 'app_blog/tags-blog.html', context={
            'title': f'#ТЭГ {tag}',
            'posts': posts,
            'common_tags': common_tags
        })
