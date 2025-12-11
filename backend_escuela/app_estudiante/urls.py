from django.urls import path
from . import views

urlpatterns = [
    # HOME
    path('', views.inicio, name='home'),

    # ESTUDIANTES
    path('estudiantes/', views.listar_estudiantes, name='ver_estudiantes'),
    path('estudiantes/agregar/', views.agregar_estudiante, name='agregar_estudiante'),
    path('estudiantes/actualizar/<int:pk>/', views.actualizar_estudiante, name='actualizar_estudiante'),
    path('estudiantes/eliminar/<int:pk>/', views.eliminar_estudiante, name='eliminar_estudiante'),

    # PROFESORES
    path('profesores/', views.listar_profesores, name='ver_profesores'),
    path('profesores/agregar/', views.agregar_profesor, name='agregar_profesor'),
    path('profesores/actualizar/<int:pk>/', views.actualizar_profesor, name='actualizar_profesor'),
    path('profesores/eliminar/<int:pk>/', views.eliminar_profesor, name='eliminar_profesor'),

    # CURSOS
    path('cursos/', views.listar_cursos, name='ver_cursos'),
    path('cursos/agregar/', views.agregar_curso, name='agregar_curso'),
    path('cursos/actualizar/<int:pk>/', views.actualizar_curso, name='actualizar_curso'),
    path('cursos/eliminar/<int:pk>/', views.eliminar_curso, name='eliminar_curso'),

    # INSCRIPCIONES
    path('inscripciones/', views.listar_inscripciones, name='ver_inscripciones'),
    path('inscripciones/agregar/', views.agregar_inscripcion, name='agregar_inscripcion'),
    path('inscripciones/actualizar/<int:pk>/', views.actualizar_inscripcion, name='actualizar_inscripcion'),
    path('inscripciones/eliminar/<int:pk>/', views.eliminar_inscripcion, name='eliminar_inscripcion'),

    # ASISTENCIAS
    path('asistencias/', views.listar_asistencias, name='ver_asistencias'),
    path('asistencias/agregar/', views.agregar_asistencia, name='agregar_asistencia'),
    path('asistencias/actualizar/<int:pk>/', views.actualizar_asistencia, name='actualizar_asistencia'),
    path('asistencias/eliminar/<int:pk>/', views.eliminar_asistencia, name='eliminar_asistencia'),

    # MATERIAS
    path('materias/', views.listar_materias, name='ver_materias'),
    path('materias/agregar/', views.agregar_materia, name='agregar_materia'),
    path('materias/actualizar/<int:pk>/', views.actualizar_materia, name='actualizar_materia'),
    path('materias/eliminar/<int:pk>/', views.eliminar_materia, name='eliminar_materia'),

    # CALIFICACIONES
    path('calificaciones/', views.listar_calificaciones, name='ver_calificaciones'),
    path('calificaciones/agregar/', views.agregar_calificacion, name='agregar_calificacion'),
    path('calificaciones/actualizar/<int:pk>/', views.actualizar_calificacion, name='actualizar_calificacion'),
    path('calificaciones/eliminar/<int:pk>/', views.eliminar_calificacion, name='eliminar_calificacion'),
]
