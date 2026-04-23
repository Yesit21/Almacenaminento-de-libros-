from django import forms
from .models import Autor, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'correo', 'nacionalidad', 'fecha_nacimiento', 'biografia']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'biografia': forms.Textarea(attrs={'rows': 4}),
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'fecha_publicacion', 'genero', 'isbn', 'autor']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
        }
