from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

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

