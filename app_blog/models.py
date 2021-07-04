from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager


class Category(models.Model):
    """Категории"""
    name = models.CharField(verbose_name="Название категория", max_length=150)
    description = RichTextUploadingField(blank=True, verbose_name='Описание категории')
    slug = models.SlugField(max_length=160, unique=True)

    # def get_absolute_url(self):
    #     return reverse_lazy('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    slug = models.SlugField()
    description = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото портфолио', blank=True)
    is_published = models.BooleanField(null=True, verbose_name='Опубликовано')
    tag = TaggableManager()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория',
                                 related_name='get_news')

    # def get_absolute_url(self):
    #     return reverse_lazy('view_news', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']
