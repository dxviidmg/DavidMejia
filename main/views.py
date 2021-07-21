from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import *

class Home(View):
	def get(self, request):
		template_name = "main/home.html"
		grados = Grado.objects.all().order_by('año_egreso')
		certificaciones = Certificacion.objects.all().order_by('año_inicio_vigencia', 'nombre', 'entidad')
		proyectos = Proyecto.objects.all().order_by('año', 'nombre')
		publicaciones = Publicacion.objects.all().order_by('año', 'titulo')
		comunidades = Comunidad.objects.all().order_by('nombre')
		fotos = Foto.objects.all().order_by('fecha')
		intereses = Interes.objects.all().order_by('nombre')

		context = {
		'grados': grados,
		'certificaciones': certificaciones,
		'proyectos': proyectos,
		'publicaciones': publicaciones,
		'comunidades': comunidades,
		'fotos': fotos,
		'intereses': intereses,
		}
		return render(request, template_name, context)