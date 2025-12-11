from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante, Profesor, Curso, Inscripcion, Asistencia, Materia, Calificacion
from .forms import EstudianteForm, ProfesorForm, CursoForm, InscripcionForm, AsistenciaForm, MateriaForm, CalificacionForm

def inicio(request):
    return render(request, 'inicio.html')

# --- ESTUDIANTES ---
def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    # Corrección: estandarizado el nombre del template
    return render(request, 'estudiante/ver_estudiantes.html', {'estudiantes': estudiantes})

def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'estudiante/agregar_estudiante.html', {'form': form})

def actualizar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('ver_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'estudiante/actualizar_estudiante.html', {'form': form})

def eliminar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    estudiante.delete()
    return redirect('ver_estudiantes')

# --- PROFESORES ---
def listar_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesor/ver_profesores.html', {'profesores': profesores})

def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_profesores')
    else:
        form = ProfesorForm()
    return render(request, 'profesor/agregar_profesor.html', {'form': form})

def actualizar_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('ver_profesores')
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'profesor/actualizar_profesor.html', {'form': form})

def eliminar_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    profesor.delete()
    return redirect('ver_profesores')

# --- CURSOS ---
def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'curso/ver_cursos.html', {'cursos': cursos})

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_cursos')
    else:
        form = CursoForm()
    return render(request, 'curso/agregar_curso.html', {'form': form})

def actualizar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('ver_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'curso/actualizar_curso.html', {'form': form})

def eliminar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    curso.delete()
    return redirect('ver_cursos')

# --- INSCRIPCIONES ---
def listar_inscripciones(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'inscripcion/ver_inscripciones.html', {'inscripciones': inscripciones})

def agregar_inscripcion(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_inscripciones')
    else:
        form = InscripcionForm()
    return render(request, 'inscripcion/agregar_inscripcion.html', {'form': form})

def actualizar_inscripcion(request, pk):
    inscripcion = get_object_or_404(Inscripcion, pk=pk)
    if request.method == 'POST':
        form = InscripcionForm(request.POST, instance=inscripcion)
        if form.is_valid():
            form.save()
            return redirect('ver_inscripciones')
    else:
        form = InscripcionForm(instance=inscripcion)
    return render(request, 'inscripcion/actualizar_inscripcion.html', {'form': form})

def eliminar_inscripcion(request, pk):
    inscripcion = get_object_or_404(Inscripcion, pk=pk)
    inscripcion.delete()
    return redirect('ver_inscripciones')

# --- ASISTENCIAS ---
def listar_asistencias(request):
    asistencias = Asistencia.objects.all()
    return render(request, 'asistencia/ver_asistencias.html', {'asistencias': asistencias})

def agregar_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_asistencias')
    else:
        form = AsistenciaForm()
    return render(request, 'asistencia/agregar_asistencia.html', {'form': form})

def actualizar_asistencia(request, pk):
    asistencia = get_object_or_404(Asistencia, pk=pk)
    if request.method == 'POST':
        form = AsistenciaForm(request.POST, instance=asistencia)
        if form.is_valid():
            form.save()
            return redirect('ver_asistencias')
    else:
        form = AsistenciaForm(instance=asistencia)
    return render(request, 'asistencia/actualizar_asistencia.html', {'form': form})

def eliminar_asistencia(request, pk):
    asistencia = get_object_or_404(Asistencia, pk=pk)
    asistencia.delete()
    return redirect('ver_asistencias')

# --- MATERIAS ---
def listar_materias(request):
    materias = Materia.objects.all()
    return render(request, 'materia/ver_materias.html', {'materias': materias})

def agregar_materia(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_materias')
    else:
        form = MateriaForm()
    return render(request, 'materia/agregar_materia.html', {'form': form})

def actualizar_materia(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    if request.method == 'POST':
        form = MateriaForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            return redirect('ver_materias')
    else:
        form = MateriaForm(instance=materia)
    return render(request, 'materia/actualizar_materia.html', {'form': form})

def eliminar_materia(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    materia.delete()
    return redirect('ver_materias')

# --- CALIFICACIONES ---
def listar_calificaciones(request):
    calificaciones = Calificacion.objects.all()
    return render(request, 'calificacion/ver_calificaciones.html', {'calificaciones': calificaciones})

def agregar_calificacion(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_calificaciones')
    else:
        form = CalificacionForm()
    return render(request, 'calificacion/agregar_calificacion.html', {'form': form})

def actualizar_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            return redirect('ver_calificaciones')
    else:
        form = CalificacionForm(instance=calificacion)
    return render(request, 'calificacion/actualizar_calificacion.html', {'form': form})

def eliminar_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    calificacion.delete()
    return redirect('ver_calificaciones')
