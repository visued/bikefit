# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0004_auto_20170222_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilatleta',
            name='nivel_atleta',
            field=models.CharField(choices=[('AM', 'Amador.'), ('AMF', 'Amador Forte.'), ('ARM', 'Alto Rendimento.'), ('ARMP', 'Alto Rendimento Profissional.'), ('RC', 'Recreacional.')], max_length=50),
        ),
    ]
