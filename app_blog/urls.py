from django.urls import path

from app_blog.views import BlogView

urlpatterns = [
    path('blog/', BlogView.as_view(), name='all_posts'),

]