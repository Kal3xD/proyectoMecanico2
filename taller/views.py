from django.shortcuts import render
from .models import info_contacto

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

def addContacto(request):
    
    if request.method != 'POST':
        generos = Genero.objects.all()
        context={"generos":generos}
        return render(request,'alumnos/alumnos_add.html',context)
    else:
        
        nombre_contacto             = request.POST["caja_nombre"]
        apellido_contacto           = request.POST["caja_apellido"]
        fecha_contacto              = request.POST["trip-start"]
        comentario_contacto         = request.POST["comentario_usuario"]
        correo_contacto             = request.POST["caja_correo"]

        obj = info_contacto.objects.create(nombre_contacto=nombre_contacto,
                                    apellido_contacto=apellido_contacto,
                                    fecha_contacto= fecha_contacto,
                                    correo_contacto=correo_contacto,
                                    comentario_contacto =comentario_contacto
                                    )
        obj.save()
        context={'mensaje':"Ok, mensaje enviado correctamente"}
        return render(request,'taller/contacto.html',context)

