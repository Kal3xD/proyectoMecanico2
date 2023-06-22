from django.db import models

# Create your models here.


class Mecanico(models.Model):
    rut              = models.CharField(primary_key = True, max_length=10)
    nombre           = models.CharField(blank=False, null=False, max_length=50)
    ap_paterno       = models.CharField(blank=False, null=False ,max_length=50)
    ap_materno       = models.CharField(blank=False, null=False, max_length=50)
    fecha_nacimiento = models.DateField(blank=False, null=False)   
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return str(self.nombre)+" "+str(self.ap_paterno)+ " " +str(self.ap_materno)   




class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)


class Atencion(models.Model):
    id_atencion         = models.AutoField(primary_key = True)
    fecha_ate           = models.DateField(blank=False, null=False , auto_now=False, auto_now_add=False)
    descripcion_ate     = models.CharField(blank=False, null=False, max_length=500)
    imagen_trabajo      = models.ImageField(upload_to=None , null = False, blank = False)
    rut                 = models.ForeignKey("Mecanico",  on_delete=models.CASCADE)
    id_estado           = models.ForeignKey("estado_atencion", on_delete=models.CASCADE, default = 2)
    id_tipo_atencion    = models.ForeignKey("tipo_atencion",  on_delete=models.CASCADE)
    


    def __str__(self):
        return  ("Atención numero") + " " +str(self.id_atencion)

class tipo_atencion (models.Model):
    id_tipo_atencion                = models.AutoField(primary_key = True)
    categoria_atencion              = models.CharField(blank = True, null = False,max_length=20)

    def __str__(self):
        return  ("Atención ") + str(self.categoria_atencion)

class estado_atencion (models.Model):
    id_estado                       = models.AutoField(primary_key = True)
    tipo_estado                     = models.CharField(blank=False, null=False, max_length= 10)

    def __str__(self):
        return str(self.tipo_estado)


class info_contacto (models.Model):
    id_contacto                     = models.AutoField(primary_key = True)
    nombre_contacto                 = models.CharField(blank = False, null = False, max_length=15)
    apellido_contacto               = models.CharField(blank = False, null = False, max_length=50)
    fecha_contacto                  = models.DateField(auto_now=False, auto_now_add=False)
    comentario_contacto             = models.CharField(blank = False, null = False, max_length=300)
    correo_contacto                 = models.EmailField(blank = False, null = False, max_length=254)

    def __str__(self):
        return 'Solicitud de contacto numero ' + str(self.id_contacto)
