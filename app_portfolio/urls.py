from django.urls import path

from app_portfolio.views import MainView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    # path('portfolio/', all_projects, name='all_projects'),

]
