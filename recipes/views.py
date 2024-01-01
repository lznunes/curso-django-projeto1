from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return  HttpResponse('''<!DOCTYPE>
    <html>
        <head><h1>Olá Mundo!</h1></head>
            <body>
                <h1>OLÁ MUNDO!</h1>
            </body>      
    </html>
''')

def contato(request):
    return  HttpResponse("Contato!")

def sobre(request):
    return  HttpResponse("Sobre!")
