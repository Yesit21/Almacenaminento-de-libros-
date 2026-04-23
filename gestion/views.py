from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Q
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

    def form_valid(self, form):
        # Verificar duplicados antes de guardar
        correo = form.cleaned_data.get('correo')
        if Autor.objects.filter(correo=correo).exists():
            messages.error(self.request, f'Ya existe un autor con el correo {correo}')
            return self.form_invalid(form)
        
        response = super().form_valid(form)
        messages.success(self.request, f'Autor "{self.object.nombre}" creado exitosamente')
        
        # Opción: Guardar y agregar otro
        if 'save_and_add' in self.request.POST:
            return redirect('autor_create')
        
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor corrige los errores en el formulario')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Nuevo Autor'
        context['boton_texto'] = 'Crear Autor'
        # Sugerencias de autores similares
        search = self.request.GET.get('nombre', '')
        if search:
            context['sugerencias'] = Autor.objects.filter(nombre__icontains=search)[:5]
        return context

class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'gestion/autor_form.html'
    success_url = reverse_lazy('autor_list')

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'gestion/autor_confirm_delete.html'
    success_url = reverse_lazy('autor_list')

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

    def form_valid(self, form):
        # Verificar ISBN duplicado
        isbn = form.cleaned_data.get('isbn')
        if Libro.objects.filter(isbn=isbn).exists():
            messages.error(self.request, f'Ya existe un libro con el ISBN {isbn}')
            return self.form_invalid(form)
        
        # Verificar si ya existe un libro con el mismo título del mismo autor
        titulo = form.cleaned_data.get('titulo')
        autor = form.cleaned_data.get('autor')
        if Libro.objects.filter(titulo=titulo, autor=autor).exists():
            messages.warning(self.request, f'Ya existe un libro "{titulo}" del autor {autor.nombre}. ¿Estás seguro de crear un duplicado?')
        
        response = super().form_valid(form)
        messages.success(self.request, f'Libro "{self.object.titulo}" creado exitosamente')
        
        # Opción: Guardar y agregar otro
        if 'save_and_add' in self.request.POST:
            return redirect('libro_create')
        
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor corrige los errores en el formulario')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Nuevo Libro'
        context['boton_texto'] = 'Crear Libro'
        # Sugerencias de libros similares
        search = self.request.GET.get('titulo', '')
        if search:
            context['sugerencias'] = Libro.objects.filter(titulo__icontains=search).select_related('autor')[:5]
        return context

class LibroUpdateView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'gestion/libro_form.html'
    success_url = reverse_lazy('libro_list')

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'gestion/libro_confirm_delete.html'
    success_url = reverse_lazy('libro_list')
