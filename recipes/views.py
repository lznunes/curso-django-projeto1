from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return  render(request, 'recipes/home.html')
    #return  render(request, 'global/home.html')
    #return  render(request, 'recipes/home.html', status=404)

    return  render(request, 'recipes/pages/home.html',context={
        'name': 'Luiz Nunes',
        } )


def recipe(request, id):
     return  render(request, 'recipes/pages/recipes-views.html',context={
        'name': 'Luiz Nunes',
        } )

