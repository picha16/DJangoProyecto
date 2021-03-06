# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 09:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eleccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
                ('votos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EscojerUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usu', models.CharField(max_length=200)),
                ('eleccion', models.CharField(max_length=200)),
                ('voto', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomusu', models.CharField(max_length=200)),
                ('data', models.DateTimeField(verbose_name='Fecha publicación usuario')),
            ],
        ),
        migrations.AddField(
            model_name='eleccion',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Usuario'),
        ),
    ]
