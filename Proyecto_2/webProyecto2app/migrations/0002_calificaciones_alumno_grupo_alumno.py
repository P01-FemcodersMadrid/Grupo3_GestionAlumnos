# Generated by Django 4.0.5 on 2022-06-30 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webProyecto2app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calificaciones',
            name='Alumno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webProyecto2app.alumno'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='Alumno',
            field=models.ManyToManyField(to='webProyecto2app.alumno'),
        ),
    ]
