from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return  render(request, 'recipes/home.html')
    #return  render(request, 'global/home.html')
    #return  render(request, 'recipes/home.html', status=404)

    return  render(request, 'recipes/home.html', status=404,context={
        'name': 'Luiz Nunes',
        } )



def contato(request):
    #return  HttpResponse("Contato!")
    return render(request, 'contatos.html')

def sobre(request):
    return  HttpResponse("Sobre!")
