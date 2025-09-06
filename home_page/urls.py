from . import views
from django.urls import path


app_name = 'home_page'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page_url'),
]
