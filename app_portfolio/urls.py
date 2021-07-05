from django.urls import path

from app_portfolio.views import HomePortfolio, PortfolioByCategory

urlpatterns = [
    path('', HomePortfolio.as_view(), name='index'),
    path('category/<str:slug>/', PortfolioByCategory.as_view(), name='category_projects')
    # path('portfolio/', ListPortfolio.as_view(), name='all_projects'),

]
