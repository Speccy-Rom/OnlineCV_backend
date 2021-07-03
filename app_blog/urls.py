from django.urls import path

from app_blog.views import all_posts

urlpatterns = [
    path('blog/', all_posts, name='all_posts'),
    # path('portfolio/', all_projects, name='all_projects'),

]