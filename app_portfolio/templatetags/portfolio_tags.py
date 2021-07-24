from django import template

from app_portfolio.models import CategoryPortfolio, Portfolio

register = template.Library()


@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return CategoryPortfolio.objects.all()


@register.inclusion_tag('app_portfolio/tag/last_projects.html')
def get_last_projects(count=6):
    projects = Portfolio.objects.order_by('created_at')[:count]
    return {'last_projects': projects}


@register.inclusion_tag('app_portfolio/tag/all_projects.html')
def get_all_projects():
    projects = Portfolio.objects.order_by('-created_at')
    return {'all_projects': projects}
