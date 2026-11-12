from django.shortcuts import render
from .models import OrdemServico
from django.shortcuts import render
from .models import OrdemServico

def lista_chamados(request):
    ordens = OrdemServico.objects.all().order_by('-data_abertura')
    context = {'ordens': ordens}
    return render(request, 'chamados/lista_chamados.html', context)

# Adiciona esta função para satisfazer o url.py
def dashboard_view(request):
    ordens = OrdemServico.objects.all().order_by('-data_abertura')
    context = {'ordens': ordens}
    return render(request, 'chamados/lista_chamados.html', context)

def lista_chamados(request):
    # Busca todas as ordens ordenadas da mais recente para a mais antiga
    ordens = OrdemServico.objects.all().order_by('-data_abertura')

    context = {
        'ordens': ordens
    }
    return render(request, 'chamados/lista_chamados.html', context)