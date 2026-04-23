from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q, Count
from .models import Autor, Libro
from .forms import AutorForm, LibroForm

# ============= VISTAS GENÉRICAS PARA AUTORES =============

class AutorListView(ListView):
    model = Autor
    template_name = 'gestion/autor_list.html'
    context_object_name = 'autores'
    paginate_by = 10

    def get_queryset(self):
        queryset = Autor.objects.annotate(total_libros=Count('libros'))
        
        # Búsqueda
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(
                Q(nombre__icontains=search) |
                Q(correo__icontains=search) |
                Q(nacionalidad__icontains=search)
            )
        
        # Filtros
        nacionalidad = self.request.GET.get('nacionalidad', '')
        if nacionalidad:
            queryset = queryset.filter(nacionalidad__icontains=nacionalidad)
        
        # Ordenamiento
        order_by = self.request.GET.get('order_by', 'nombre')
        direction = self.request.GET.get('direction', 'asc')
        
        if direction == 'desc':
            order_by = f'-{order_by}'
        
        queryset = queryset.order_by(order_by)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        context['nacionalidad'] = self.request.GET.get('nacionalidad', '')
        context['order_by'] = self.request.GET.get('order_by', 'nombre')
        context['direction'] = self.request.GET.get('direction', 'asc')
        context['total_autores'] = self.get_queryset().count()
        
        # Obtener todas las nacionalidades únicas para el filtro
        context['nacionalidades'] = Autor.objects.values_list('nacionalidad', flat=True).distinct().order_by('nacionalidad')
        
        # Calcular rango de resultados mostrados
        page_obj = context['page_obj']
        start = (page_obj.number - 1) * self.paginate_by + 1
        end = min(start + self.paginate_by - 1, context['total_autores'])
        context['start_index'] = start
        context['end_index'] = end
        
        return context

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

# ============= VISTAS GENÉRICAS PARA LIBROS =============

class LibroListView(ListView):
    model = Libro
    template_name = 'gestion/libro_list.html'
    context_object_name = 'libros'
    paginate_by = 10

    def get_queryset(self):
        queryset = Libro.objects.select_related('autor')
        
        # Búsqueda
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(
                Q(titulo__icontains=search) |
                Q(isbn__icontains=search) |
                Q(autor__nombre__icontains=search)
            )
        
        # Filtros
        genero = self.request.GET.get('genero', '')
        if genero:
            queryset = queryset.filter(genero__icontains=genero)
        
        autor_id = self.request.GET.get('autor', '')
        if autor_id:
            queryset = queryset.filter(autor_id=autor_id)
        
        # Ordenamiento
        order_by = self.request.GET.get('order_by', 'titulo')
        direction = self.request.GET.get('direction', 'asc')
        
        if direction == 'desc':
            order_by = f'-{order_by}'
        
        queryset = queryset.order_by(order_by)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        context['genero'] = self.request.GET.get('genero', '')
        context['autor_filtro'] = self.request.GET.get('autor', '')
        context['order_by'] = self.request.GET.get('order_by', 'titulo')
        context['direction'] = self.request.GET.get('direction', 'asc')
        context['total_libros'] = self.get_queryset().count()
        
        # Obtener todos los géneros únicos para el filtro
        context['generos'] = Libro.objects.values_list('genero', flat=True).distinct().order_by('genero')
        
        # Obtener todos los autores para el filtro
        context['autores'] = Autor.objects.all().order_by('nombre')
        
        # Calcular rango de resultados mostrados
        page_obj = context['page_obj']
        start = (page_obj.number - 1) * self.paginate_by + 1
        end = min(start + self.paginate_by - 1, context['total_libros'])
        context['start_index'] = start
        context['end_index'] = end
        
        return context

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
