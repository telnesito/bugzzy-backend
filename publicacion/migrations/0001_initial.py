# Generated by Django 4.2.7 on 2023-12-26 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0008_remove_usuarios_nada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('fechaPublicacion', models.DateTimeField(auto_created=True)),
                ('idPublicacion', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('tituloPublicacion', models.CharField(max_length=100)),
                ('descripcionPublicacion', models.TextField()),
                ('tipoPublicacion', models.CharField(max_length=100)),
                ('miniatura', models.FileField(upload_to='miniatura/')),
                ('cedulaCreador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='capitulosPublicacion',
            fields=[
                ('idVideoPublicacion', models.AutoField(primary_key=True, serialize=False)),
                ('video_url', models.FileField(upload_to='videos/')),
                ('tituloCapitulo', models.CharField(max_length=100)),
                ('idPublicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicacion.publicacion')),
            ],
        ),
    ]
