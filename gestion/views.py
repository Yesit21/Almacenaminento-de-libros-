from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Autor, Libro
from .forms import AutorForm, LibroForm

# ============= VISTAS GENÉRICAS PARA AUTORES =============

class AutorListView(ListView):
    model = Autor
    template_name = 'gestion/autor_list.html'
    context_object_name = 'autores'
    paginate_by = 10

class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'gestion/autor_form.html'
    success_url = reverse_lazy('autor_list')

class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'gestion/autor_form.html'
    success_url = reverse_lazy('autor_list')

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'gestion/autor_confirm_delete.html'
    success_url = reverse_lazy('autor_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Autor eliminado correctamente")
        return super().delete(request, *args, **kwargs)

# ============= VISTAS GENÉRICAS PARA LIBROS =============

class LibroListView(ListView):
    model = Libro
    template_name = 'gestion/libro_list.html'
    context_object_name = 'libros'
    paginate_by = 10

class LibroCreateView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'gestion/libro_form.html'
    success_url = reverse_lazy('libro_list')

class LibroUpdateView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'gestion/libro_form.html'
    success_url = reverse_lazy('libro_list')

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'gestion/libro_confirm_delete.html'
    success_url = reverse_lazy('libro_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Libro eliminado correctamente")
        return super().delete(request, *args, **kwargs)
