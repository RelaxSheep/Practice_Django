from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class HomePage(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'home_page/home_page.html')