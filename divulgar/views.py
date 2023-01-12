from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Tag, Raca, Pet
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
@login_required
def novo_pet(request):
    
    if request.method == "GET":
        tags = Tag.objects.all()
        racas = Raca.objects.all()
        return render(request,'novo_pet.html', {'tags': tags, 'racas': racas})
    
    
    elif request.method == "POST":
        foto = request.FILES.get('foto')
        nome = request.POST.get('nome')
        sexo = request.POST.get('sexo')
        descricao = request.POST.get('descricao')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        telefone = request.POST.get('telefone')
        tags = request.POST.getlist('tags')
        raca = request.POST.get('raca')
        
        #VALIDAR TUDO 
        tags = Tag.objects.all()
        racas = Raca.objects.all()
        if len(nome.strip()) == 0 or len(sexo.strip()) == 0 or len(descricao.strip()) == 0 or len(telefone.strip()) == 0 or len(raca.strip()) == 0:  #Falta validar a foto estar vazia
            messages.add_message(request, constants.ERROR, "Preencha todos os campos !")
            return render(request,'novo_pet.html', {'tags': tags, 'racas': racas})
        
        pet = Pet(
            usuario = request.user,
            foto=foto,
            nome=nome,
            sexo=sexo,
            descricao=descricao,
            estado=estado,
            cidade=cidade,
            telefone=telefone,
            raca_id=raca,
        )
        
        pet.save()
        
        for tag_id in tags:
            tag = Tag.objects.get(id=tag_id)
            pet.tags.add(tag)
        
        messages.add_message(request, constants.SUCCESS, 'Novo pet cadastrado')
        return render(request, 'novo_pet.html', {'tags': tags, 'racas': racas})