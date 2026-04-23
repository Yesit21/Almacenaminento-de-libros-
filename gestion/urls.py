from django.urls import path
from . import views

urlpatterns = [
    # Home Dashboard
    path('', views.HomeView.as_view(), name='home'),
    
    # URLs para Autores
    path('autores/', views.AutorListView.as_view(), name='autor_list'),
    path('autores/crear/', views.AutorCreateView.as_view(), name='autor_create'),
    path('autores/editar/<int:pk>/', views.AutorUpdateView.as_view(), name='autor_update'),
    path('autores/eliminar/<int:pk>/', views.AutorDeleteView.as_view(), name='autor_delete'),
    
    # URLs para Libros
    path('libros/', views.LibroListView.as_view(), name='libro_list'),
    path('libros/crear/', views.LibroCreateView.as_view(), name='libro_create'),
    path('libros/editar/<int:pk>/', views.LibroUpdateView.as_view(), name='libro_update'),
    path('libros/eliminar/<int:pk>/', views.LibroDeleteView.as_view(), name='libro_delete'),
]
