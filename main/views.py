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

		print(proyectos)
		context = {
		'grados': grados,
		'certificaciones': certificaciones,
		'proyectos': proyectos,
		'publicaciones': publicaciones,
		}
		return render(request, template_name, context)