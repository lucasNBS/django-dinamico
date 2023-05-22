from django.shortcuts import render
from .models import Filme, Locacao

# Create your views here.
def index(request):
    return render(request, "locadora/index.html")

def filmes(request):
    filmes = Filme.objects.all()
    context = {"filmes": filmes}
    return render(request, "locadora/filmes.html", context)

def locacao(request):
    locacao = Locacao.objects.all()
    context = {"locacoes": locacao}
    return render(request, "locadora/locacao.html", context)