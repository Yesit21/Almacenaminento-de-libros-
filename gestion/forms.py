from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Autor, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'correo', 'nacionalidad', 'fecha_nacimiento', 'biografia']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo del autor'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
            'nacionalidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'País de origen'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'biografia': forms.Textarea(attrs={
                'rows': 4,
                'class': 'form-control',
                'placeholder': 'Breve biografía del autor (opcional)'
            }),
        }
        labels = {
            'nombre': 'Nombre Completo',
            'correo': 'Correo Electrónico',
            'nacionalidad': 'Nacionalidad',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'biografia': 'Biografía'
        }
        help_texts = {
            'correo': 'El correo debe ser único',
            'fecha_nacimiento': 'Formato: DD/MM/AAAA'
        }
    
    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data.get('fecha_nacimiento')
        if fecha and fecha > date.today():
            raise ValidationError('La fecha de nacimiento no puede ser futura')
        if fecha and fecha.year < 1900:
            raise ValidationError('La fecha de nacimiento debe ser posterior a 1900')
        return fecha
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre and len(nombre) < 3:
            raise ValidationError('El nombre debe tener al menos 3 caracteres')
        return nombre

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'fecha_publicacion', 'genero', 'isbn', 'autor']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del libro'
            }),
            'fecha_publicacion': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'genero': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Ficción, Ciencia, Historia'
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ISBN-13 o ISBN-10'
            }),
            'autor': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
        labels = {
            'titulo': 'Título del Libro',
            'fecha_publicacion': 'Fecha de Publicación',
            'genero': 'Género Literario',
            'isbn': 'ISBN',
            'autor': 'Autor'
        }
        help_texts = {
            'isbn': 'El ISBN debe ser único',
            'fecha_publicacion': 'Formato: DD/MM/AAAA'
        }
    
    def clean_fecha_publicacion(self):
        fecha = self.cleaned_data.get('fecha_publicacion')
        if fecha and fecha > date.today():
            raise ValidationError('La fecha de publicación no puede ser futura')
        if fecha and fecha.year < 1450:
            raise ValidationError('La fecha debe ser posterior a la invención de la imprenta (1450)')
        return fecha
    
    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if isbn:
            # Remover guiones y espacios
            isbn_limpio = isbn.replace('-', '').replace(' ', '')
            if not isbn_limpio.isdigit():
                raise ValidationError('El ISBN solo debe contener números y guiones')
            if len(isbn_limpio) not in [10, 13]:
                raise ValidationError('El ISBN debe tener 10 o 13 dígitos')
        return isbn
    
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if titulo and len(titulo) < 2:
            raise ValidationError('El título debe tener al menos 2 caracteres')
        return titulo

