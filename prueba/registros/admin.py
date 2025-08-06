from django.contrib import admin
from .models import Alumnos
from .models import Comentario
from .models import ComentarioContacto

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')  #
    list_display= ('matricula', 'nombre', 'carrera', 'turno', 'created') 
    search_fields  = ('matricula', 'nombre', 'carrera', 'turno')  #coloca la barra de busqueda
    date_hierarchy = 'created'  
    list_filter= ('carrera', 'turno')  #filtro para agrupar datos

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Usuarios2').exists():
            return ('created', 'updated', 'matricula', 'carrera', 'turno')
        else:
            return ('created', 'updated')
            


admin.site.register(Alumnos, AdministrarModelo)  # registra el modelo Alumnos con la clase AdministrarModelo

class AdministrarComentario(admin.ModelAdmin):
    list_display=('id', 'created', 'coment')
    csearch_fields=('id', 'created', 'coment')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='PermisoComentarios').exists():
            return ('created', 'alumno'  )
        else:
            return ('created', )
        
    

admin.site.register(Comentario, AdministrarComentario)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)