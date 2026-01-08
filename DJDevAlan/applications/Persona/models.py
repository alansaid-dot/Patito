from django.db import models
from ckeditor.fields import RichTextField
from applications.departamento.models import Departamento

class Habilidades(models.Model):
    habilidad=models.CharField('Habilidad', max_length=50)
    
    class meta:
        verbose_name='Habilidades'
        verbose_name_plural='Habilidades empleados'
    
    def __str__(self):
        return str(self.id)+'-'+self.habilidad


class Empleado(models.Model):
    JOB_CHOICES=(
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )
    
    first_name=models.CharField('Nombre', max_length=60)
    last_name=models.CharField('Apellidos', max_length=60)
    full_name=models.CharField('Nombre completo', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    Habilidades=models.ManyToManyField(Habilidades)
    hoja_vida=RichTextField()
    
    class meta:
        verbose_name='Mi Empleado'
        verbose_name_plurarl='Empleados de la empresa'
        ordering=['-first_name','last_name']
        unique_together=('first_name', 'Departamento')
    
    def __str__(self):
        return str (self.id)+'-'+ self.first_name +'-'+ self.last_name