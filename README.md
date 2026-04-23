# Sistema de Gestión de Libros - Django

Proyecto Django para la gestión de autores y libros con relaciones de base de datos.

## Características

- CRUD completo para Autores y Libros
- Vistas genéricas de Django (ListView, CreateView, UpdateView, DeleteView)
- Interfaz con Bootstrap 5
- Panel de administración de Django
- Relación ForeignKey entre Autor y Libro

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/Yesit21/Almacenaminento-de-libros-.git
cd Almacenaminento-de-libros-
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Realizar migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Crear superusuario:
```bash
python manage.py createsuperuser
```

6. Ejecutar servidor:
```bash
python manage.py runserver
```

## Estructura del Proyecto

```
proyecto/
├── gestion/              # Aplicación principal
│   ├── models.py         # Modelos Autor y Libro
│   ├── views.py          # Vistas genéricas CRUD
│   ├── forms.py          # Formularios
│   ├── urls.py           # URLs de la app
│   ├── admin.py          # Configuración admin
│   └── templates/        # Plantillas HTML
├── proyecto/             # Configuración del proyecto
│   ├── settings.py
│   └── urls.py
└── manage.py
```

## URLs Disponibles

### Autores
- `/autores/` - Lista de autores
- `/autores/crear/` - Crear autor
- `/autores/editar/<id>/` - Editar autor
- `/autores/eliminar/<id>/` - Eliminar autor

### Libros
- `/libros/` - Lista de libros
- `/libros/crear/` - Crear libro
- `/libros/editar/<id>/` - Editar libro
- `/libros/eliminar/<id>/` - Eliminar libro

### Admin
- `/admin/` - Panel de administración

## División de Trabajo (Ramas)

- **Estudiante 1**: ListView (rama: `feature/list-view`)
- **Estudiante 2**: DeleteView (rama: `feature/delete-view`)
- **Estudiante 3**: UpdateView (rama: `feature/update-view`)
- **CreateView**: Base del proyecto

## Tecnologías

- Python 3.14
- Django 6.0.4
- Bootstrap 5
- SQLite

## Autores

Proyecto desarrollado por el equipo de desarrollo.
