# Generated by Django 4.2.7 on 2023-12-26 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_usuarios_clave'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='nada',
            field=models.CharField(default='nul'),
            preserve_default=False,
        ),
    ]
