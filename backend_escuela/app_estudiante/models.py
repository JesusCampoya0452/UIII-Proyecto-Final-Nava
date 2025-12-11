from django.db import models

# -------------------------
#       ESTUDIANTE
# -------------------------
class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    num_matricula = models.CharField(max_length=20)
    fecha_inscripcion = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# -------------------------
#         PROFESOR
# -------------------------
class Profesor(models.Model):
    id_profesor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    dni = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# -------------------------
#          CURSO
# -------------------------
class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=100)
    descripcion = models.TextField()
    creditos = models.IntegerField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    horario = models.CharField(max_length=100)
    aula = models.CharField(max_length=50)
    nivel_educativo = models.CharField(max_length=50)
    costo_curso = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_curso

# -------------------------
#        INSCRIPCION
# -------------------------
class Inscripcion(models.Model):
    id_inscripcion = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()
    estado_inscripcion = models.CharField(max_length=50)
    nota_final = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Inscripción {self.id_inscripcion}"

# -------------------------
#         ASISTENCIA
# -------------------------
class Asistencia(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_clase = models.DateField()
    presente = models.BooleanField(default=False)
    justificacion = models.TextField(null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Asistencia {self.id_asistencia}"

# -------------------------
#          MATERIA
# -------------------------
class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True)
    nombre_materia = models.CharField(max_length=100)
    descripcion = models.TextField()
    profesor = models.ManyToManyField(Profesor)
    nivel_academico = models.CharField(max_length=50)
    es_obligatoria = models.BooleanField(default=True)
    horas_semanales = models.IntegerField()

    def __str__(self):
        return self.nombre_materia

# -------------------------
#       CALIFICACION
# -------------------------
class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    tipo_evaluacion = models.CharField(max_length=50)
    fecha_evaluacion = models.DateField()
    puntaje = models.DecimalField(max_digits=5, decimal_places=2)
    ponderacion = models.DecimalField(max_digits=3, decimal_places=2)
    comentarios = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Calificación {self.id_calificacion}"