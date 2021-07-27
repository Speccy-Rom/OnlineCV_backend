from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from taggit.managers import TaggableManager
from django.utils import timezone

from app_portfolio.models import Category


class Category(models.Model):
    """Категории"""
    name = models.CharField(verbose_name="Название категория", max_length=150, db_index=True)
    description = RichTextUploadingField(blank=True, verbose_name='Описание категории')
    slug = models.SlugField(max_length=160, unique=True)

    def get_absolute_url(self):
        return reverse_lazy('category_posts', kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название', db_index=True)
    slug = models.SlugField(unique=True)
    description = RichTextUploadingField(verbose_name='Контент', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото портфолио', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    tag = TaggableManager()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория',
                                 related_name='get_news')

    def get_absolute_url(self):
        return reverse_lazy('view_post', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    text = models.TextField(verbose_name='Комментарий')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_date']

    def __str__(self):
        return self.text
