from django.shortcuts import render

# Create your views here.

def bienvenida(request):
    return render(request, 'data/bienvenida.html', {})


def prov(request):
    return render(request, 'data/prov.html', {})
