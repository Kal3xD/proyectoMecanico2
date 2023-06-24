from django.shortcuts import render
from .models import info_contacto, Mecanico, tipo_atencion, Atencion
from django.db.models import Q
from django.contrib.auth.decorators import login_required

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

def vistasMecanico(request):
    context={}
    return render(request, 'taller/vistasMecanico.html', context)

def Mecanico1(request):
    context={}
    return render(request, 'taller/Mecanico1.html', context)

def Mecanico2(request):
    context={}
    return render(request, 'taller/Mecanico2.html', context)

def Mecanico3(request):
    context={}
    return render(request, 'taller/Mecanico3.html', context)

def login(request):
    context={}
    return render(request, 'taller/login.html', context)

def creacion(request):
    context={}
    return render(request, 'taller/creacion.html', context)

@login_required
def menu(request):
    request.session["usuario"] =request.user.username
    usuario = request.session["usuario"]
    context = {"usuario":usuario}
    return render(request, 'taller/index.html',context)

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

def busqueda(request):
    context={}
    return render(request,'taller/busqueda.html', context)

def buscar(request):
   if request.method == 'GET':
        query = request.GET.get('q')
        context={}

        if query and query.lower()== "juan":
            return render(request,'taller/Mecanico1.html', context)
        
        elif query and query.lower() == "pedro":
            return render(request,'taller/Mecanico2.html', context)

        elif query and query.lower() == "andres":
            return render(request,'taller/Mecanico3.html', context)
        

        elif query and query.lower() == "motor":
            return render(request,'taller/chequeoMotor.html', context)
        
        elif query and query.lower() == "electronico":
            return render(request,'taller/sistemaElectronico.html', context)

        elif query and query.lower() == "direccionales":
            return render(request,'taller/jsDireccionales.html', context)
           

        else:
            resultados = []

            return render(request, 'taller/busqueda.html', {'resultados': resultados})

def addAtencion(request):
    
    if request.method != 'POST':
        generos = Genero.objects.all()
        context={"generos":generos}
        return render(request,'alumnos/alumnos_add.html',context)
        
    else:
        
        nombre_mecanico                 = request.POST["selec_mecanico"]
        imagen_atencion                 = request.POST["imagen_proce"]
        fecha_atencion                  = request.POST["trip-Fecha"]
        desc_atencion                   = request.POST["comentario_proce"]
        tipo_atencion                   = request.POST["tipoAtencion"]

        obj = Atencion.objects.create(id_tipo_atencion  =  tipo_atencion,
                                    fecha_ate           =  fecha_atencion,
                                    descripcion_ate     =  desc_atencion,
                                    imagen_trabajo      =  imagen_atencion,
                                    rut                 =  nombre_mecanico,
                                    )
        obj.save()
        context={'mensaje':"Ok, mensaje enviado correctamente"}
        return render(request,'taller/index.html',context)

def desplegable_mecanico(request):

    opciones_mecanico = Mecanico.objects.all()

    return render(request, 'taller/nuevas_atenciones.html', {'opciones_mecanico': opciones_mecanico}) 