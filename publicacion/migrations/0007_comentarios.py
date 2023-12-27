# Generated by Django 4.2.7 on 2023-12-27 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_remove_usuarios_nada'),
        ('publicacion', '0006_capitulospublicacion_miniatura_publicacion_miniatura_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('idComentarioPublicacion', models.AutoField(primary_key=True, serialize=False)),
                ('comentario', models.CharField(max_length=366)),
                ('cedulaComentarista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuarios')),
                ('idPublicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicacion.publicacion')),
            ],
        ),
    ]
