from django.db import models


class Departamento(models.Model):
    nombre=models.TextField('Nombre',max_length=50)
    subnombre=models.TextField('Nombre_corto',max_length=30)
    activo = models.BooleanField('Anulado', default='False')
    

    class Meta:
        verbose_name='Mi Departamento'
        verbose_name_plural='Areas de la empresa'
        ordering=['-nombre']
        unique_together=('nombre','subnombre')
    
    def __str__(self):
        return self.nombre + ' - ' + self.subnombre
    
