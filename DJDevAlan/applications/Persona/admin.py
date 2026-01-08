from django.contrib import admin
from .models import Empleado, Habilidades

admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        'first_name',
        'last_name',
        'job',
        'full_name',
        'id'
    )
    
    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    search_fields=('first_name',)
    list_filter=('departamento','job','Habilidades')
    
    filter_horizontal=('Habilidades',)
    
    

admin.site.register(Empleado, EmpleadoAdmin)
