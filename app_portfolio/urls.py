from django.urls import path

from app_portfolio.views import ListPortfolio, PortfolioByCategory, ViewProjects, HomePage, TagView, FeedBackView


urlpatterns = [
    path('', FeedBackView.as_view(), name='contact'),
    path('', HomePage.as_view(), name='index'),
    path('portfolio/', ListPortfolio.as_view(), name='list_projects'),
    path('portfolio/<str:slug>', ViewProjects.as_view(), name='view_projects'),
    path('portfolio/tag/<str:slug>/', TagView.as_view(), name='tag_projects'),
    path('portfolio/category/<str:slug>/', PortfolioByCategory.as_view(), name='category_projects'),


]
