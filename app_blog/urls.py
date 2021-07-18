from django.urls import path

from app_blog.views import BlogByCategory, HomeBlog, ViewPosts, TagView

urlpatterns = [
    path('', HomeBlog.as_view(), name='all_posts'),
    path('tag/<str:slug>/', TagView.as_view(), name='tags_blog'),
    path('category/<str:slug>/', BlogByCategory.as_view(), name='category_posts'),
    path('<str:slug>', ViewPosts.as_view(), name='view_post'),
]
