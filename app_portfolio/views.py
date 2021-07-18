from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from taggit.models import Tag

from app_portfolio.forms import FeedBackForm
from app_portfolio.models import Portfolio, Category


class HomePage(View):
    def get(self, request, *args, **kwargs):
        projects = Portfolio.objects.all()
        return render(request, 'index.html', {'projects': projects, 'title': 'Home'})


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
        posts = Portfolio.objects.filter(stack=tag)
        common_tags = Portfolio.stack.most_common()
        return render(request, 'app_portfolio/tags-projects.html', context={
            'title': f'#ТЭГ {tag}',
            'posts': posts,
            'common_tags': common_tags
        })


class FeedBackView(View):
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        return render(request, 'index.html', context={
            'form': form,
            'title': 'Home'
        })

    def post(self, request, *args, **kwargs):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(f'От {name} | {subject}', message, from_email, ['nimda.xd@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок')
            return HttpResponseRedirect('success')
        return render(request, 'index.html', context={
            'form': form,
        })
