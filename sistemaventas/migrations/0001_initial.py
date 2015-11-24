# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=10)),
                ('categoria', models.ForeignKey(to='sistemaventas.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=10)),
                ('marca', models.ForeignKey(to='sistemaventas.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
                ('precio', models.CharField(max_length=10)),
                ('ubicacion', models.CharField(max_length=30)),
                ('fecha_pu', models.DateTimeField(auto_now=True)),
                ('imagen', models.ImageField(upload_to=b'publicaciones')),
                ('Modelo', models.ForeignKey(to='sistemaventas.Modelo')),
                ('marca', models.ForeignKey(to='sistemaventas.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='publicacion',
            name='usuario',
            field=models.ForeignKey(to='sistemaventas.Usuario'),
        ),
    ]
