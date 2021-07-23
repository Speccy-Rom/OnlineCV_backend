from rest_framework import viewsets, permissions, pagination
from rest_framework.response import Response

from .serializers import PostSerializer, ProjectSerializer
from app_blog.models import Blog
from app_portfolio.models import Portfolio


# Create your views here.
class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    ordering = "created_at"


class PostViewSet(viewsets.ModelViewSet):
    """Вывод списка постов"""

    serializer_class = PostSerializer
    queryset = Blog.objects.all()
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberSetPagination


class ProjectViewSet(viewsets.ModelViewSet):
    """Вывод всех проектов"""

    serializer_class = ProjectSerializer
    queryset = Portfolio.objects.all()
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberSetPagination