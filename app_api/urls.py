from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, ProjectViewSet, TagDetailView, StackDetailView, TagsView, CategoryPortfolioView,\
    LastPostView, LastProjectsView, FeedBackView, RegisterView, ProfileView

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('projects', ProjectViewSet, basename='projects')

urlpatterns = [
    path('', include(router.urls)),
    path('tags/', TagsView.as_view()),
    # path('blog/category/', CategoryBlogView.as_view()),
    path('portfolio/category/', CategoryPortfolioView.as_view()),
    path('blog/tags/<slug:tag_slug>/', TagDetailView.as_view()),
    path('portfolio/tags/<slug:tag_slug>/', StackDetailView.as_view()),
    path('last_posts/', LastPostView.as_view()),
    path('last_projects/', LastProjectsView.as_view()),
    path('feedback/', FeedBackView.as_view()),
    path('register/', RegisterView.as_view()),
    # path('profile/', ProfileView.as_view()),

]
