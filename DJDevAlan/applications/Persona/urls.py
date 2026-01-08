from django.urls import path
from . import views

app_name="persona_app"

urlpatterns = [
    path(
        '', 
        views.InicioView.as_view(),
        name='inicio'
    ),
    path('Listar-todos-empleados/', views.LisAllEmpleados.as_view(), name='empleados_all'),
    path('lista-by-area/<subnombre>/', views.ListByAreaEmpleado.as_view(), name='empleados_area'),
    path('buscar-empleado/', views.listEmpleadoByKword.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadosDetailView.as_view(), name='empleado_detail'),
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name='empleado_add'),
    path('lista-habilidades-empleado/', views.ListHabilidadesEmpleado.as_view()),
    path(
        'success/', 
        views.SuccessView.as_view(), 
        name='correcto'
    ),
    path(
        'update-empleado/<pk>', 
        views.EmpleadoUpdateView.as_view(), 
        name='Modificar_empleado'
    ),
    path(
        'delete-empleado/<pk>', 
        views.EmpleadoDeleteView.as_view(), 
        name='Eliminar_Empleado'
    ),
    path(
        'lista-empleados-admin/', 
        views.ListaEmpleadosAdmin.as_view(), 
        name='empleados_admin'
    ),
    
]