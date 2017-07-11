from django.db import models

class Grado(models.Model):
	titulo = models.CharField(max_length=100)
	institucion = models.CharField(max_length=100)
	cedula = models.CharField(max_length=10)
	año_egreso = models.CharField(max_length=4)

	def __str__(self):
		return self.titulo

	class Meta:
		ordering = ['año_egreso',]

class Certificacion(models.Model):
	nombre = models.CharField(max_length=100)
	entidad = models.CharField(max_length=100)
	año = models.CharField(max_length=4)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ['año', 'nombre']
			
class Proyecto(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField()
	imagen = models.ImageField(upload_to="proyectos/%Y/%m/%d/")
	enlace = models.CharField(max_length=100, blank=True, null=True)
	año = models.IntegerField()

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ['año', 'nombre']

class Comunidad(models.Model):
	nombre = models.CharField(max_length=30)
	logo = models.ImageField(upload_to="comunidades/%Y/%m/%d/")
	enlace_fb = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre

	class meta:
		ordering = ['nombre']

class Publicacion(models.Model):
	
	Tipo_choices = (
		("Publicación científica", "Publicación Científica"),
		("Blog", "Blog"),
	)
	
	titulo = models.CharField(max_length=200)
	lugar = models.TextField()
	tipo = models.CharField(max_length=30, choices=Tipo_choices)
	año = models.CharField(max_length=4)
	enlace = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.titulo

	class meta:
		ordering = ['año', 'titulo']

class Foto(models.Model):
	imagen = models.ImageField(upload_to="fotos/%Y/%m/%d/")
	descripcion = models.CharField(max_length=100)
	fecha = models.DateField()

	def __str__(self):
		return self.descripcion

	class meta:
		ordering = ['fecha']

class Interes(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre

	class meta:
		ordering = ['nombre']