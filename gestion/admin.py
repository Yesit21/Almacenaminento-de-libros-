from django.contrib import admin
from .models import Autor, Libro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'nacionalidad', 'fecha_nacimiento')
    search_fields = ('nombre', 'correo', 'nacionalidad')
    list_filter = ('nacionalidad', 'fecha_nacimiento')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'fecha_publicacion', 'autor', 'isbn')
    list_filter = ('autor', 'genero', 'fecha_publicacion')
    search_fields = ('titulo', 'isbn', 'autor__nombre')
