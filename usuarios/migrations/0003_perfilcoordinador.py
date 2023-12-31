# Generated by Django 4.2.7 on 2023-11-25 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_perfilestudiante_cedulaestudiante_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilCoordinador',
            fields=[
                ('idPerfilCoordinador', models.AutoField(primary_key=True, serialize=False)),
                ('experienciaCoordinador', models.CharField(max_length=244)),
                ('materiaCoordinador', models.CharField(max_length=244)),
                ('fraseCoordinador', models.CharField(max_length=244)),
                ('sobreCoordinador', models.CharField(max_length=244)),
                ('cedulaCoordinador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuarios')),
            ],
        ),
    ]
