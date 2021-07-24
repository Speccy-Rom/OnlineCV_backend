from rest_framework import generics, viewsets, permissions, pagination
from rest_framework.response import Response
from taggit.models import Tag

from .serializers import PostSerializer, ProjectSerializer, TagSerializer, CategoryBlogSerializer, \
    CategoryPortfolioSerializer
from app_blog.models import Blog, CategoryBlog
from app_portfolio.models import Portfolio, CategoryPortfolio


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


class TagDetailView(generics.ListAPIView):
    """Вывод постов блога по тегу"""
    serializer_class = PostSerializer
    pagination_class = PageNumberSetPagination
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug'].lower()
        tag = Tag.objects.get(slug=tag_slug)
        return Blog.objects.filter(tag=tag)


class StackDetailView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    pagination_class = PageNumberSetPagination
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug'].lower()
        tag = Tag.objects.get(slug=tag_slug)
        return Portfolio.objects.filter(stack=tag)


class TagsView(generics.ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [permissions.AllowAny]


class CategoryBlogView(generics.ListAPIView):
    serializer_class = CategoryBlogSerializer
    queryset = CategoryBlog.objects.all()
    permission_classes = [permissions.AllowAny]


class CategoryPortfolioView(generics.ListAPIView):
    serializer_class = CategoryPortfolioSerializer
    queryset = CategoryPortfolio.objects.all()
    permission_classes = [permissions.AllowAny]
