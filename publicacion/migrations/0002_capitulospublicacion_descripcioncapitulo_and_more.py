# Generated by Django 4.2.7 on 2023-12-26 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='capitulospublicacion',
            name='descripcionCapitulo',
            field=models.CharField(default='Null', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='capitulospublicacion',
            name='miniatura',
            field=models.FileField(default='Null', upload_to='videos/miniatura/'),
            preserve_default=False,
        ),
    ]
