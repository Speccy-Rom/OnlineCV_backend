from django.contrib import admin

from .models import Blog, Category


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'category')
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    save_on_top = True  # управление навигацие отобразится сверху
    save_as = True
    list_editable = ("category",)  # редактирование поля в таблице списков проектов
    fieldsets = (
        (None, {
            'fields': (('title', 'slug'),)
        }),
        (None, {
            'fields': ('description', 'image'),
        }),

        ('Tags & Category', {
            'classes': ('collapse',),
            'fields': (('stack', 'category'),)
        }),
        ('Demo & Website project', {
            'classes': ('collapse',),
            'fields': (('website', 'demo'),)
        }),

    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('id', 'name')



