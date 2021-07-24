from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Blog, CategoryBlog, Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_image', 'title', 'created_at', 'updated_at', 'is_published', 'category', 'tag')
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    # list_filter = ('category', 'created_at')
    # readonly_fields = ("get_image",)
    search_fields = ('title', 'description')
    save_on_top = True  # управление навигацией отобразится сверху
    save_as = True
    list_editable = ("category", 'is_published', 'tag')  # редактирование поля в таблице списков проектов
    fieldsets = (
        (None, {
            'fields': (('title', 'slug'),)
        }),
        (None, {
            'fields': ('description', 'image'),
        }),
        ('Tags & Category', {
            'classes': ('collapse',),
            'fields': (('tag', 'author', 'category'),)
        }),

        (None, {
            'fields': ('is_published',),
        }),

    )

    ####################################
    # Вывод картинок в админку #
    ####################################
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="90" height="50"')

    get_image.short_description = "Изображение"
    ####################################


@admin.register(CategoryBlog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('id', 'name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'text', 'created_date')
    list_display_links = ('id', 'post')