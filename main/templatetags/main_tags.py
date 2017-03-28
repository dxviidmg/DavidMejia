from django import template 
register = template.Library()
from ..models import *

@register.simple_tag
def MisProyectos():
	return Proyecto.objects.all()

@register.simple_tag
def MisComunidades():
	comunidades = Comunidad.objects.all()
	return comunidades
	
@register.simple_tag
def MisGrados():
	return Grado.objects.all()