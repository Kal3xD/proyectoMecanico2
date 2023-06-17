from django.contrib import admin
from .models import Mecanico, Genero, Atencion, estado_atencion

# Register your models here.

admin.site.register(Mecanico)
admin.site.register(Genero)
admin.site.register(Atencion)
admin.site.register(estado_atencion)