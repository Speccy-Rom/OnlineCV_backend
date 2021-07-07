from django.urls import path

from app_blog.views import BlogByCategory, HomeBlog, ViewPosts

urlpatterns = [
    path('blog/', HomeBlog.as_view(), name='all_posts'),
    path('blog/category/<slug:slug>/', BlogByCategory.as_view(), name='category_posts'),
    path('blog/<slug:slug>', ViewPosts.as_view(), name='view_post'),
]
