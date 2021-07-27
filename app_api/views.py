from rest_framework import generics, viewsets, permissions, pagination, filters
from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.response import Response
from taggit.models import Tag

from .serializers import PostSerializer, ProjectSerializer, TagSerializer, CategoryPortfolioSerializer, \
    ContactSerializer, RegisterSerializer, UserSerializer, CommentSerializer
from app_blog.models import Blog, Category, Comment
from app_portfolio.models import Portfolio, Category


# Create your views here.
class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    ordering = "created_at"


class PostViewSet(viewsets.ModelViewSet):
    """Вывод списка постов"""

    search_fields = ['$title', '$description']
    filter_backends = (filters.SearchFilter,)
    serializer_class = PostSerializer
    queryset = Blog.objects.all()
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberSetPagination


class ProjectViewSet(viewsets.ModelViewSet):
    """Вывод всех проектов"""

    search_fields = ['$title', '$description']
    filter_backends = (filters.SearchFilter,)
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


# class CategoryBlogView(generics.ListAPIView):
#     serializer_class = CategoryBlogSerializer
#     queryset = Category.objects.all()
#     permission_classes = [permissions.AllowAny]


class CategoryPortfolioView(generics.ListAPIView):
    serializer_class = CategoryPortfolioSerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]


class LastPostView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Blog.objects.order_by('-id')[:3]
    permission_classes = [permissions.AllowAny]


class LastProjectsView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Portfolio.objects.order_by('id')[:3]
    permission_classes = [permissions.AllowAny]


class FeedBackView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = ContactSerializer(data=request.data)
        if serializer_class.is_valid():
            data = serializer_class.validated_data
            name = data.get('name')
            from_email = data.get('email')
            subject = data.get('subject')
            message = data.get('message')
            send_mail(f'От {name} | {subject}', message, from_email, ['nimda.xd@gmail.com'])
            return Response({"success": "Sent"})


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'message': 'Пользователь создан успешно'
        })


class ProfileView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({
            'user': UserSerializer(request.user, context=self.get_renderer_context()).data,
        })


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_slug = self.kwargs['post_slug'].lower()
        post = Blog.objects.get(slug=post_slug)
        return Comment.objects.filter(post=post)
