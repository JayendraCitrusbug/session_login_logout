from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.core.serializers import serialize
from django.views import View
import json


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(username=username)
        if check_password(password, user.password):
            request.session['username'] = user.username
            return redirect('home')
        else :
            return redirect('login')

class HomeView(View):
    def get(self, request):
        username = request.session.get('username')
        if username:
            return render(request, "home.html" , {'user':User.objects.get(username=username)})
        else:
            return redirect('login')

class LogoutView(View):
    def get(self, request):
        request.session.flush()
        return redirect('login')