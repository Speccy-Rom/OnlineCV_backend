from django import template

from app_portfolio.models import Category, Portfolio

register = template.Library()


@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return Category.objects.all()


@register.inclusion_tag('app_portfolio/includes/last_projects.html')
def get_last_projects():
    projects = Portfolio.objects.order_by('id')[:3]
    return {'last_projects': projects}
