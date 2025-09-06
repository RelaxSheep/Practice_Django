from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate


# Create your views here.
class LoginPage(View):
    def get(self, request):
        return render(request, 'login/login_page.html')
    def post(self, request):
        next_url = request.POST.get('next') or request.GET.get('next') or '/'
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        user = authenticate(username=user_name, password=password)
        success = True
        if(user is None):
            success = False
            return render(request, 'login/login_page.html', {'success' : success})
        else:
            login(request, user)
            return redirect(next_url)