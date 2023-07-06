from django.shortcuts import render
from .models import info_contacto, Mecanico, tipo_atencion, Atencion, estado_atencion
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



def desplegable_mecanico(request):

    opciones_mecanico = Mecanico.objects.all()

    return render(request, 'taller/nuevas_atenciones.html', {'opciones_mecanico': opciones_mecanico}) 

def lista_atenciones(request):
    atenciones= Atencion.objects.all()
    context={"atenciones":atenciones}
    return render(request, 'taller/lista_atenciones.html', context)

def encontrar_atencion(request, pk):
    if pk != "":
        atenciones= Atencion.objects.get(id_atencion=pk)
        
        mecanicos= Mecanico.objects.all()
        tipos_atenciones= tipo_atencion.objects.all()
        estados_atenciones= estado_atencion.objects.all()

        
        context={'atenciones': atenciones, 'mecanicos': mecanicos, 'tipos_atenciones': tipos_atenciones, 'estados_atenciones': estados_atenciones}

        if atenciones:
            return render(request, 'taller/modificar_atenciones.html', context)
        else:
            context={'mensaje': "Error, Atencion no existe."}
            return render(request,'taller/lista_atenciones.html' )

def modificar_atencion(request):

    if request.method == "POST":

        id_atencion= request.POST["id_atencion"]
        fecha_ate= request.POST["fechaAten"]
        descripcion_ate= request.POST["Descripcion"]
        rut =request.POST["mecanico"]
        id_estado = request.POST["estado"]
        id_tipo_atencion = request.POST["tipo_atencion"]
        activo="1"
        
        objMecanico= Mecanico.objects.get(rut = rut)
        objEstado_atencion= estado_atencion.objects.get(id_estado = id_estado)
        objTipo_atencion = tipo_atencion.objects.get(id_tipo_atencion = id_tipo_atencion)

        atencion = Atencion()
        atencion.id_atencion= id_atencion
        atencion.fecha_ate= fecha_ate
        atencion.descripcion_ate= descripcion_ate
        atencion.rut=  objMecanico
        atencion.id_estado= objEstado_atencion
        atencion.id_tipo_atencion= objTipo_atencion
        atencion.activo=1
        atencion.save()

        mecanicos = Mecanico.objects.all()
        estados_atenciones = estado_atencion.objects.all()
        tipos_atenciones = tipo_atencion.objects.all()

        context={'mensaje':"Datos actualizados", 'mecanicos':mecanicos, 'estados_atenciones':estados_atenciones, 'tipos_atenciones':tipos_atenciones}
        return render(request, 'taller/modificar_atenciones.html',context)

    else:
        atenciones= Atencion.objects.all()
        context={"atenciones":atenciones}
        return render(request, 'taller/lista_atenciones.html', context)


def borrar_atencion(request, pk):
    context={}
    try: 
        atencion= Atencion.objects.get(id_atencion=pk)

        atencion.delete()
        mensaje = "Registro eliminado"
        atenciones = Atencion.objects.all()
        context={'atenciones': atenciones, 'mensaje':mensaje}
        return render(request, 'taller/lista_atenciones.html', context)
    
    except:
        mensaje= "Error, Id de atención no existe"
        atenciones = Atencion.objects.all()
        context={'atenciones': atenciones, 'mensaje':mensaje}
        return render(request, 'taller/lista_atenciones.html', context)
        
def nuevas_atenciones(request):
    if request.method != "POST":
        mecanicos= Mecanico.objects.all()
        tipos_atenciones= tipo_atencion.objects.all()
        estados_atenciones= estado_atencion.objects.all()

        context={'mecanicos':mecanicos,'tipos_atenciones':tipos_atenciones, 'estados_atenciones':estados_atenciones }
        return render(request, 'taller/nuevas_atenciones.html', context)

    else:
        id_atencion= request.POST["id_atencion"]
        fecha_ate= request.POST["fechaAten"]
        descripcion_ate= request.POST["Descripcion"]
        imagen_trabajo= request.POST["imagen"]
        rut =request.POST["mecanico"]
        id_estado = request.POST["valor_deseado"]
        id_tipo_atencion = request.POST["tipo_atencion"]
        
        objMecanico= Mecanico.objects.get(rut = rut)
        objEstado_atencion= estado_atencion.objects.get(id_estado = id_estado)
        objTipo_atencion = tipo_atencion.objects.get(id_tipo_atencion = id_tipo_atencion)

        obj= Atencion.objects.create(
            id_atencion=id_atencion,
            fecha_ate=fecha_ate,
            descripcion_ate=descripcion_ate,
            imagen_trabajo=imagen_trabajo,
            rut=objMecanico,
            id_estado=objEstado_atencion,
            id_tipo_atencion=objTipo_atencion)
        
        obj.save()
        context={'mensaje':'Atencion agregada'}
        return render(request, 'taller/nuevas_atenciones.html', context)


    