from django.contrib import admin
from .models import Estudiante, Profesor, Curso, Inscripcion, Asistencia, Materia, Calificacion


class MateriaAdmin(admin.ModelAdmin):
    filter_horizontal = ('profesor',)


# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Inscripcion)
admin.site.register(Asistencia)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Calificacion)
