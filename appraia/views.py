from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  
from appraia.models import *


# Create your views here.
def logar_usuario(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        exist_user_name = Usuario.objects.filter(nome=username)
        exist_user_password = Usuario.objects.filter(senha=password)
        print(exist_user_password)
        if exist_user_name and exist_user_password :
            return redirect('main')
        else:
            messages.error(request,'Login ou senha não estão corretos')
            return redirect('logar_usuario')

    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})

def main(request):
    return render(request,'index.html')

def create_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_create = Usuario.objects.create(nome=username, email=email, senha=password)
    return render(request, 'create_user.html')