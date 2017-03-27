from django.db import models

class Proyecto(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField()
	imagen = models.ImageField(upload_to="proyecto/%Y/%m/%d/")
	enlace = models.CharField(max_length=100, blank=True, null=True)
	año = models.IntegerField()

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ['año', 'nombre']

class Comunidad(models.Model):
	nombre = models.CharField(max_length=30)
	logo = models.ImageField(upload_to="comunidad/%Y/%m/%d/")
	enlace_fb = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre

	class meta:
		ordering = ['nombre']