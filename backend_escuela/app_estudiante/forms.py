
from django import forms
from .models import Estudiante, Profesor, Curso, Inscripcion, Asistencia, Materia, Calificacion

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'fecha_inscripcion': forms.DateInput(attrs={'type': 'date'}),
        }

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'
        widgets = {
            'fecha_contratacion': forms.DateInput(attrs={'type': 'date'}),
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = '__all__'
        widgets = {
            'fecha_inscripcion': forms.DateInput(attrs={'type': 'date'}),
        }

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'
        widgets = {
            'fecha_clase': forms.DateInput(attrs={'type': 'date'}),
        }

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'
        widgets = {
            'profesor': forms.CheckboxSelectMultiple,
        }

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = '__all__'
        widgets = {
            'fecha_evaluacion': forms.DateInput(attrs={'type': 'date'}),
        }
