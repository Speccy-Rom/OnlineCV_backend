from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse_lazy
from taggit.managers import TaggableManager


class Category(models.Model):
    """Категории"""
    name = models.CharField(verbose_name="Название категория", max_length=150)
    description = RichTextUploadingField(blank=True, verbose_name='Описание')
    slug = models.SlugField(max_length=160, unique=True)

    def get_absolute_url(self):
        return reverse_lazy('category_projects', kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Portfolio(models.Model):
    """Модель проекта"""
    title = models.CharField(max_length=250, verbose_name='Название')
    slug = models.SlugField(max_length=160, unique=True)
    description = RichTextUploadingField(verbose_name='Описание проекта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото проекта', blank=True)
    stack = TaggableManager()
    website = models.URLField(max_length=250, blank=True, verbose_name='GitHub')
    demo = models.URLField(max_length=250, blank=True, verbose_name='Демо')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория',
                                 related_name='get_news')

    def get_absolute_url(self):
        return reverse_lazy('view_projects', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-created_at']
