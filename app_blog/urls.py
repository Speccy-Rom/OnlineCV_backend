from django.urls import path

from app_blog.views import BlogByCategory, HomeBlog, ViewPosts

urlpatterns = [
    path('blog/', HomeBlog.as_view(), name='all_posts'),
    path('blog/category/<str:slug>/', BlogByCategory.as_view(), name='category_posts'),
    path('blog/<str:slug>', ViewPosts.as_view(), name='view_post'),
]