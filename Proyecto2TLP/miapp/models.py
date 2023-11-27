from django.db import models
from django.contrib.auth.models import User, Group

TIPO_CHOICES = [('V', 'Vacaciones'),
                ( 'F' ,'Feriado'),
                ('Sa','Suspension de actividades'),
                ('Sap','Suspension de actividades PM'),
                ('P' ,'Periodo lectivo'), 
                ('Se','Suspension de evaluaciones'),
                ('C','Ceremonia'),
                ('Ed', 'EDDA') ,
                ('Ev','Evaluacion'),
                ('A','Ayudantias'), 
                ('H','Hito academico'),
                ('Sec','Secretaria academica'),
                ('O','OAI'), 
                ]

CAT_CHOICES = [('C','Comunidad USM'),
                ('E','Estudiante'),
                ('P','Profesor'), 
               ('J',"Jefe de carrera"), ]


class Evento(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    descripcion = models.CharField(max_length=150)
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES)
    segmento = models.ManyToManyField(Group)


    def __str__(self) -> str:
        return self.titulo


