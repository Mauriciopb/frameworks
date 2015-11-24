# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechacomentario', models.DateTimeField(auto_now_add=True)),
                ('autor', models.CharField(max_length=100)),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='publicacion',
            old_name='Modelo',
            new_name='modelo',
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_pu',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='precio',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='comentario',
            name='idpublicacion',
            field=models.ForeignKey(to='sistemaventas.Publicacion'),
        ),
    ]
