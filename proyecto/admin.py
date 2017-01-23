from django.contrib import admin

from .models import Usuario, Eleccion, EscojerUsuario

class UsuarioAdmin(admin.ModelAdmin):
	campos=[
	('Informacion nombre',{'campos':['nomusu']}),
	('Informacion fecha',{'campos':['data']}),
	]
class EleccionAdmin(admin.ModelAdmin):
        campos=[
        ('Informacion de texto',{'campos':['nombre','texto']}), 
        ('Informacion votos',{'campos':['votos']}),
        ]
class EscojerUsuarioAdmin(admin.ModelAdmin):
        campos=[
        ('Informacion de texto',{'campos':['usu','eleccion']}), 
        ('Informacion votos',{'campos':['voto']}),
        ]

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Eleccion, EleccionAdmin)
admin.site.register(EscojerUsuario, EscojerUsuarioAdmin)
# Register your models here.
