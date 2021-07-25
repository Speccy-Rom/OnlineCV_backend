from django import template

from app_blog.models import Blog, Category

register = template.Library()


@register.simple_tag()
def get_categories():
    """Вывод всех категорий блога"""
    return Category.objects.all()


@register.inclusion_tag('app_blog/tag/last_posts.html')
def get_last_posts(count=6):
    posts = Blog.objects.order_by('-id')[:count]
    return {'last_posts': posts}
