# Generated by Django 4.2.6 on 2023-11-27 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('titulo', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('descripcion', models.CharField(max_length=150)),
                ('tipo', models.CharField(choices=[('V', 'Vacaciones'), ('F', 'Feriado'), ('Sa', 'Suspension de actividades'), ('Sap', 'Suspension de actividades PM'), ('P', 'Periodo lectivo'), ('Se', 'Suspension de evaluaciones'), ('C', 'Ceremonia'), ('Ed', 'EDDA'), ('Ev', 'Evaluacion'), ('A', 'Ayudantias'), ('H', 'Hito academico'), ('Sec', 'Secretaria academica'), ('O', 'OAI')], max_length=100)),
                ('segmento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Eventos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
