from django.db import models

# Create your models here.

class Candidatos (models.Model):
    id_candidato=models.CharField(max_length=10, blank=False,primary_key=True)
    nombre=models.CharField(max_length=100, blank=False)
    apellido=models.CharField(max_length=100, blank=False)
    fecha_nacimiento=models.DateField(blank=False)
    genero=models.CharField(max_length=1, blank=False)
    def _str_(self):
        return self.nombre 
    

class Puestos (models.Model):
    id_puesto=models.CharField(max_length=10, blank=False, primary_key=True)
    titulo=models.CharField(max_length=25, blank=False)
    descripcion=models.TextField()
    salario=models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    fecha_apertura=models.DateField(blank=False)

    def _str_(self):
        return self.titulo
    
class Vacantes (models.Model):  
    id_vacante=models.CharField(max_length=10, blank=False, primary_key=True)
    id_candidato=models.ForeignKey(Candidatos, on_delete=models.RESTRICT)
    id_puesto=models.ForeignKey(Puestos, on_delete=models.RESTRICT)
    fecha_solicitud=models.DateField(blank=False)

    def _str_(self):
        return self.id_vacante
    
class Resueltas (models.Model):
    id_respuesta=models.CharField(max_length=10, blank=False, primary_key=True)
    id_vacante=models.ForeignKey(Vacantes, on_delete=models.RESTRICT)
    id_candidato=models.ForeignKey(Candidatos, on_delete=models.RESTRICT)
    calificacion=models.IntegerField(blank=False)
    fecha_respuesta=models.DateField(blank=False)
    
    def _str_(self):
        return self.id_respuesta