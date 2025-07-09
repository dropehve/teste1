from django.shortcuts import render

def index (request):
    return render(request, 'index.html')
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def sua_view(request):
    return render(request, 'tema/sua_pagina.html')

from django.shortcuts import render
from .models import Lesao  # substitua pelo nome real do seu modelo

def listar_dados(request):
    dados = Lesao.objects.all()
    return render(request, 'tema/lista.html', {'dados': dados})
