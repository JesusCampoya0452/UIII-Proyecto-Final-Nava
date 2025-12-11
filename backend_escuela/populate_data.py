import os
import django
import sys
from faker import Faker
import random
from datetime import date

# Añadir el directorio raíz del proyecto al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_escuela.settings')
django.setup()

from app_estudiante.models import Estudiante, Profesor, Curso, Inscripcion, Asistencia, Materia, Calificacion

fake = Faker('es_ES')

def create_data():
    # Crear Estudiantes
    for _ in range(3):
        Estudiante.objects.create(
            nombre=fake.first_name(),
            apellido=fake.last_name(),
            fecha_nacimiento=fake.date_of_birth(minimum_age=18, maximum_age=30),
            genero=random.choice(['M', 'F']),
            direccion=fake.address(),
            telefono=fake.phone_number(),
            email=fake.email(),
            num_matricula=str(fake.unique.random_number(digits=10)),
            fecha_inscripcion=fake.date_this_year()
        )

    # Crear Profesores
    for _ in range(3):
        Profesor.objects.create(
            nombre=fake.first_name(),
            apellido=fake.last_name(),
            email=fake.email(),
            telefono=fake.phone_number(),
            especialidad=fake.job(),
            fecha_contratacion=fake.date_this_decade(),
            salario=random.uniform(30000.0, 80000.0),
            dni=str(fake.unique.random_number(digits=8))
        )

    # Crear Materias
    for _ in range(3):
        Materia.objects.create(
            nombre_materia=fake.bs(),
            descripcion=fake.text(),
            nivel_academico=random.choice(['Básico', 'Intermedio', 'Avanzado']),
            es_obligatoria=fake.boolean(),
            horas_semanales=random.randint(2, 6)
        )

    # Get objects to create relationships
    profesores = list(Profesor.objects.all())
    
    # Crear Cursos
    for _ in range(3):
        Curso.objects.create(
            nombre_curso=fake.catch_phrase(),
            descripcion=fake.text(),
            creditos=random.randint(2, 5),
            profesor=random.choice(profesores),
            horario=fake.time(pattern='%H:%M'),
            aula=f"Aula {random.randint(100, 500)}",
            nivel_educativo=random.choice(['Pregrado', 'Posgrado']),
            costo_curso=random.uniform(500.0, 2000.0)
        )
        
    # Get objects for relationships
    estudiantes = list(Estudiante.objects.all())
    cursos = list(Curso.objects.all())

    # Crear Inscripciones
    for _ in range(3):
        Inscripcion.objects.create(
            estudiante=random.choice(estudiantes),
            curso=random.choice(cursos),
            fecha_inscripcion=fake.date_this_year(),
            estado_inscripcion=random.choice(['Inscrito', 'En curso', 'Completado', 'Retirado']),
            nota_final=random.uniform(0.0, 10.0)
        )

    # Crear Asistencias
    for _ in range(3):
        Asistencia.objects.create(
            estudiante=random.choice(estudiantes),
            curso=random.choice(cursos),
            fecha_clase=fake.date_this_month(),
            presente=fake.boolean(),
            justificacion=fake.sentence() if random.choice([True, False]) else "",
            comentarios=fake.sentence()
        )

    # Get objects for relationships
    inscripciones = list(Inscripcion.objects.all())
    
    # Crear Calificaciones
    for _ in range(3):
        Calificacion.objects.create(
            inscripcion=random.choice(inscripciones),
            tipo_evaluacion=random.choice(['Parcial', 'Final', 'Trabajo Práctico']),
            fecha_evaluacion=fake.date_this_month(),
            puntaje=random.uniform(0.0, 10.0),
            ponderacion=random.uniform(0.1, 0.5),
            comentarios=fake.text()
        )

if __name__ == '__main__':
    print("Limpiando la base de datos...")
    Calificacion.objects.all().delete()
    Asistencia.objects.all().delete()
    Inscripcion.objects.all().delete()
    Curso.objects.all().delete()
    Materia.objects.all().delete()
    Profesor.objects.all().delete()
    Estudiante.objects.all().delete()
    
    print("Creando nuevos datos...")
    create_data()
    print("¡Datos falsos creados exitosamente!")
