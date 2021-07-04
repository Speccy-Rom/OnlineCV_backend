from django.contrib import admin

from .models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'category')
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('id', 'name')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
