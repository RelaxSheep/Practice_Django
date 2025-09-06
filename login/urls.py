from django.urls import path
from . import views


app_name = 'login'

urlpatterns = [
    path('', views.LoginPage.as_view(), name='login_page'),
]
