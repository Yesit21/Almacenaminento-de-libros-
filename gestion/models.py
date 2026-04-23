from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    biografia = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20, unique=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
    
    def __str__(self):
        return self.titulo
