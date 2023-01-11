from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
import re
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

regex_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

# Create your views here.
def cadastro(request):
    # if request.user.is_authenticate:
    #     return redirect('/divulgar/novo_pet')
    
    if request.method == "GET":
        return render(request, '../templates/cadastro.html')
    elif request.method == "POST":
        name = request.POST.get("nome")
        email = request.POST.get("email")
        password = request.POST.get("senha")
        conf_password = request.POST.get("confirmar_senha")
        if len(name.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0 or len(conf_password.strip()) == 0:
            messages.add_message(request, constants.ERROR, "Preencha todos os campos !")
            return render(request, 'cadastro.html')
        
        if password != conf_password:
            messages.add_message(request, constants.ERROR, "As senhas não conferem !")
            return render(request, 'cadastro.html')

        if not re.fullmatch(regex_email, email):
            messages.add_message(request, constants.ERROR, "Digite um e-mail válido !")
            return render(request, 'cadastro.html')
            
        try:
            user = User.objects.create_user(
                username=name,
                email=email,
                password=password,
            )
            messages.add_message(request, constants.SUCCESS, "Usuário criado com sucesso !")
            return render(request, 'cadastro.html')
        except:
            messages.add_message(request, constants.ERROR, "Erro interno no systema !")
            return render(request, 'cadastro.html')
        
        
def logar(request):
    # if request.user.is_authenticate:
    #     return redirect('/divulgar/novo_pet')
    
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(username=nome,
                            password=senha)
        
    if user is not None:
        login(request, user)
        return redirect('/divulgar/novo_pet')
    else:
        messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
        return render(request, 'login.html')
    

def sair(request):
    logout(request)
    return redirect('/auth/login')