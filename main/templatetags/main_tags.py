from django import template 
register = template.Library()
from ..models import *

@register.simple_tag
def MisProyectos():
	proyectos = Proyecto.objects.all()
	return proyectos

@register.simple_tag
def MisComunidades():
	comunidades = Comunidad.objects.all()
	return comunidades