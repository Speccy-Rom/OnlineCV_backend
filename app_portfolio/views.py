from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from app_portfolio.models import Portfolio, Category


# class MainView(View):
#     def get(self, request, *args, **kwargs):
#         context = {}
#         posts = Portfolio.objects.all()
#         projects = Portfolio.objects.all()
#         context['posts'] = posts
#         context['projects'] = projects
#         return render(request, 'index.html', context)
#

class PortfolioByCategory(ListView):
    model = Portfolio
    template_name = 'index.html'
    context_object_name = 'cat_projects'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PortfolioByCategory, self).get_context_data()
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])

    def get_queryset(self):
        return Portfolio.objects.filter(slug=self.kwargs['slug'])


class HomePortfolio(ListView):
    model = Portfolio
    template_name = 'index.html'
    context_object_name = 'projects'
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomePortfolio, self).get_context_data()
        context['title'] = 'Home'
        return context

    # def get_queryset(self):
    #     return Portfolio.objects.all()[0:3]


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

