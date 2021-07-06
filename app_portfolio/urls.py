from django.urls import path

from app_portfolio.views import HomePortfolio, PortfolioByCategory, ViewProjects

urlpatterns = [
    path('', HomePortfolio.as_view(), name='index'),
    path('portfolio/category/<str:slug>/', PortfolioByCategory.as_view(), name='category_projects'),
    path('portfolio/<str:slug>', ViewProjects.as_view(), name='view_projects'),

]
