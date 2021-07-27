from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from django.contrib.auth.models import User
from taggit.models import Tag

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


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)
        lookup_field = 'name'
        extra_kwargs = {
            'url': {'lookup_field': 'name'}
        }


# class CategoryBlogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'slug', 'description')
#         lookup_field = 'slug'
#         extra_kwargs = {
#             'url': {'lookup_field': 'name'}
#         }


class CategoryPortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'name'}
        }


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()
    subject = serializers.CharField()
    message = serializers.CharField()


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2',
        ]

    extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        password2 = validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})
        user = User(username=username)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    post = serializers.SlugRelatedField(slug_field='slug', queryset=Blog.objects.all())

    class Meta:
        model = Comment
        fields = ('id', 'post', 'username', 'text', 'created_date')
        lookup_fields = 'id'
        extra_kwargs = {
            'url': {'lookup_fields': 'id'}
        }
