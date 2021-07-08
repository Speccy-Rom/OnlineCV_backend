from django.urls import path

from app_portfolio.views import ListPortfolio, PortfolioByCategory, ViewProjects, HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('portfolio/category/<slug:slug>/', PortfolioByCategory.as_view(), name='category_projects'),
    path('portfolio/', ListPortfolio.as_view(), name='list_projects'),
    path('portfolio/<slug:slug>', ViewProjects.as_view(), name='view_projects'),

]
