from django.urls import path

from app_blog.views import BlogByCategory, HomeBlog, ViewPosts

urlpatterns = [
    path('', HomeBlog.as_view(), name='all_posts'),
    path('category/<slug:slug>/', BlogByCategory.as_view(), name='category_posts'),
    path('<slug:slug>', ViewPosts.as_view(), name='view_post'),
]
