# Generated by Django 4.2.6 on 2023-11-27 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_segmento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='segmento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Eventos', to='miapp.segmento'),
        ),
    ]
