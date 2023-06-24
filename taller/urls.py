from django.urls import path
from . import views



urlpatterns = [
    path('index', views.index, name='index'),
    path('chequeoMotor', views.chequeoMotor, name='chequeoMotor'),
    path('contacto', views.contacto, name='contacto'),
    path('jsDireccionales', views.jsDireccionales, name='jsDireccionales'),
    path('nuevas_atenciones', views.nuevas_atenciones, name='nuevas_atenciones'),
    path('sistemasElectronico', views.sistemaElectronico, name='sistemaElectronico'),
    path('addContacto',views.addContacto,name='addContacto'),
    path('busqueda',views.busqueda, name='busqueda'),
    path('buscar', views.buscar, name='buscar'),
    path('vistasMecanico', views.vistasMecanico, name='vistasMecanico'),
    path('Mecanico1', views.Mecanico1, name='Mecanico1'),
    path('Mecanico2', views.Mecanico2, name='Mecanico2'),
    path('Mecanico3', views.Mecanico3, name='Mecanico3'),
    path('login', views.login, name='login'),
    path('creacion', views.creacion, name='creacion'),
    path('addAtencion',views.addAtencion,name='addAtencion'),
    path('desplegable_mecanico', views.desplegable_mecanico, name ='desplegable_mecanico')


]