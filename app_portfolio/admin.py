from django.contrib import admin

from .models import Category, Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'stack', 'category')
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('id', 'name')


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Category, CategoryAdmin)
