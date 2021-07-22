from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from django.contrib.auth.models import User

from app_blog.models import Blog, Category, Comment


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tag = TagListSerializerField()
    author = serializers.SlugRelatedField(slug_field='User', queryset='User.objects.all()')

    class Meta:
        model = Blog
        fields = ('id', 'title', 'slug', 'description', 'image', 'created_at', 'updated_at', 'is_published', 'author',
                  'tag', 'category')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
