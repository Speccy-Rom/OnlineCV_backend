from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import PostSerializer
from app_blog.models import Blog


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Blog.objects.all()
    lookup_field = 'slug'
