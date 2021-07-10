from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from taggit.models import Tag

from app_portfolio.models import Portfolio, Category


class HomePage(View):
    def get(self, request, *args, **kwargs):
        projects = Portfolio.objects.all()
        return render(request, 'index.html', {'projects': projects})


class PortfolioByCategory(ListView):
    model = Portfolio
    template_name = 'index.html'
    context_object_name = 'get_categories'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PortfolioByCategory, self).get_context_data()
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])

    def get_queryset(self):
        return Portfolio.objects.filter(slug=self.kwargs['slug'])


class ListPortfolio(ListView):
    model = Portfolio
    template_name = 'app_portfolio/page-portfolio.html'
    context_object_name = 'projects'

    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListPortfolio, self).get_context_data()
        context['title'] = 'My projects'
        return context


class ViewProjects(DetailView):
    model = Portfolio
    template_name = 'app_portfolio/page-portfolio-detail.html'
    context_object_name = 'detail_project'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = Portfolio.objects.get(slug=self.kwargs['slug'])

    def get_queryset(self):
        return Portfolio.objects.filter(slug=self.kwargs['slug'])


class TagView(View):
    def get(self, request, slug, *args, **kwargs):
        tag = get_object_or_404(Tag, slug=slug)
        posts = Portfolio.objects.filter(tag=tag)
        common_tags = Portfolio.stack.most_common()
        return render(request, 'app_portfolio/tag/tag_portfolio.html', context={
            'title': f'#ТЭГ {tag}',
            'posts': posts,
            'common_tags': common_tags
        })
