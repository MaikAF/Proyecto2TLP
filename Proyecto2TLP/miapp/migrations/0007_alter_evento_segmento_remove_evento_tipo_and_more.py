# Generated by Django 4.2.6 on 2023-11-27 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('miapp', '0006_tipo_remove_evento_tipo_evento_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='segmento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Eventos', to='auth.group'),
        ),
        migrations.RemoveField(
            model_name='evento',
            name='tipo',
        ),
        migrations.DeleteModel(
            name='Segmento',
        ),
        migrations.DeleteModel(
            name='Tipo',
        ),
        migrations.AddField(
            model_name='evento',
            name='tipo',
            field=models.CharField(choices=[('V', 'Vacaciones'), ('F', 'Feriado'), ('Sa', 'Suspension de actividades'), ('Sap', 'Suspension de actividades PM'), ('P', 'Periodo lectivo'), ('Se', 'Suspension de evaluaciones'), ('C', 'Ceremonia'), ('Ed', 'EDDA'), ('Ev', 'Evaluacion'), ('A', 'Ayudantias'), ('H', 'Hito academico'), ('Sec', 'Secretaria academica'), ('O', 'OAI')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
