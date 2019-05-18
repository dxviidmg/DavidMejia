from django.contrib import admin
from .models import *

class CertificacionAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'entidad', "año"]

class FotoAdmin(admin.ModelAdmin):
	list_display = ['descripcion', 'fecha']

class ProyectoAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'año']	

admin.site.register(Grado)
admin.site.register(Certificacion, CertificacionAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Comunidad)
admin.site.register(Publicacion)
admin.site.register(Foto, FotoAdmin)
admin.site.register(Interes)