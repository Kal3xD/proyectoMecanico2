from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'taller/index.html', context)


def chequeoMotor(request):
    context={}
    return render(request, 'taller/chequeoMotor.html', context)

def contacto(request):
    context={}
    return render(request, 'taller/contacto.html', context)

def nuevas_atenciones(request):
    context={}
    return render(request, 'taller/nuevas_atenciones.html', context)

def sistemaElectronico(request):
    context={}
    return render(request, 'taller/sistemaElectronico.html', context)

def jsDireccionales(request):
    context={}
    return render(request, 'taller/jsDireccionales.html', context)