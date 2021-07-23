from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from django.contrib.auth.models import User

from app_blog.models import Blog, Category, Comment
from app_portfolio.models import Portfolio, Category


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tag = TagListSerializerField()
    author = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        model = Blog
        fields = ('id', 'title', 'slug', 'description', 'image', 'created_at', 'updated_at', 'is_published', 'author',
                  'tag', 'category')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class ProjectSerializer(TaggitSerializer, serializers.ModelSerializer):
    stack = TagListSerializerField()

    class Meta:
        model = Portfolio
        fields = ('id', 'title', 'slug', 'description', 'image', 'created_at', 'updated_at', 'website', 'demo',
                  'stack', 'category')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }