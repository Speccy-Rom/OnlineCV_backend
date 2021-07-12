from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_image', 'title', 'created_at', 'updated_at', 'stack', 'category')
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    # list_filter = ('category', 'created_at')
    # readonly_fields = ("get_image", )
    search_fields = ('title', 'description', 'category__name')
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

    ####################################
    # Вывод картинок в админку #
    ####################################
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="90" height="50"')

    get_image.short_description = "Изображение"
    ####################################


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('id', 'name', 'slug')


admin.site.site_title = 'Django OnlineCV'
admin.site.site_header = 'Django OnlineCV'
