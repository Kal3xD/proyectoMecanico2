from django.urls import path
from . import views



urlpatterns = [
    path('index', views.index, name='index'),
    path('chequeoMotor', views.chequeoMotor, name='chequeoMotor'),
    path('contacto', views.contacto, name='contacto'),
    path('jsDireccionales', views.jsDireccionales, name='jsDireccionales'),
    
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
    path('desplegable_mecanico', views.desplegable_mecanico, name ='desplegable_mecanico'),
    
    path('lista_atenciones', views.lista_atenciones, name='lista_atenciones'),
    path('encontrar_atencion/<str:pk>', views.encontrar_atencion, name='encontrar_atencion'),
    path('modificar_atencion', views.modificar_atencion, name='modificar_atencion'),
    path('borrar_atencion/<str:pk>', views.borrar_atencion, name='borrar_atencion'),
    path('nuevas_atenciones', views.nuevas_atenciones, name='nuevas_atenciones')


]