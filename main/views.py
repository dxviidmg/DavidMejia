from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import *

class Home(View):
	def get(self, request):
		template_name = "main/home.html"
		grados = Grado.objects.all()
		certificaciones = Certificacion.objects.all()
		proyectos = Proyecto.objects.all()
		publicaciones = Publicacion.objects.all()
		comunidades = Comunidad.objects.all()
		fotos = Foto.objects.all()
		intereses = Interes.objects.all()

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