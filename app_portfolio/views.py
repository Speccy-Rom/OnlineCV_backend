from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from app_blog.models import Blog
from app_portfolio.models import Portfolio, Category


# class MainView(View):
#     def get(self, request, *args, **kwargs):
#         context = {}
#         posts = Blog.objects.all()
#         projects = Portfolio.objects.all()
#         context['posts'] = posts
#         context['projects'] = projects
#         return render(request, 'index.html', context)


class PortfolioByCategory(ListView):
    model = Portfolio
    template_name = 'index.html'
    context_object_name = 'projects'

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
