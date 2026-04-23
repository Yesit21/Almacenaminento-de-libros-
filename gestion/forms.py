from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils import timezone
from .models import Autor, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'correo', 'nacionalidad', 'fecha_nacimiento', 'biografia']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'biografia': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_correo(self):
        correo = (self.cleaned_data.get('correo') or '').strip()
        validate_email(correo)
        return correo

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        if fecha_nacimiento is None:
            return fecha_nacimiento

        hoy = timezone.localdate()
        if fecha_nacimiento > hoy:
            raise ValidationError('La fecha de nacimiento no puede ser futura.')

        if fecha_nacimiento.year < 1800:
            raise ValidationError('La fecha de nacimiento debe ser mayor o igual al año 1800.')

        return fecha_nacimiento

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'fecha_publicacion', 'genero', 'isbn', 'autor']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_fecha_publicacion(self):
        fecha_publicacion = self.cleaned_data.get('fecha_publicacion')
        if fecha_publicacion is None:
            return fecha_publicacion

        hoy = timezone.localdate()
        if fecha_publicacion > hoy:
            raise ValidationError('La fecha de publicación no puede ser futura.')

        return fecha_publicacion

    def validate_unique(self):
        exclude = self._get_validation_exclusions()
        if not self.instance.pk:
            exclude.add('isbn')

        try:
            self.instance.validate_unique(exclude=exclude)
        except ValidationError as e:
            self._update_errors(e)
