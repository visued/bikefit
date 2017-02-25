# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0006_auto_20170222_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilatleta',
            name='modalidade_principal',
            field=models.CharField(choices=[('', '---Modalide principal.---'), ('', 'MTB.'), ('', 'Ciclismo.'), ('', 'Triathlon.'), ('', 'Outros.')], max_length=50),
        ),
        migrations.AlterField(
            model_name='perfilatleta',
            name='nivel_atleta',
            field=models.CharField(choices=[('', '---Nível do atleta.---'), ('', 'Amador.'), ('', 'Amador Forte.'), ('', 'Alto Rendimento.'), ('', 'Alto Rendimento Profissional.'), ('', 'Recreacional.')], max_length=50),
        ),
        migrations.AlterField(
            model_name='perfilatleta',
            name='tipo_de_relevo',
            field=models.CharField(choices=[('', '---Tipo relevo.---'), ('', 'Plano.'), ('', 'Pouco de subidas.'), ('', 'Muitas subidas.')], max_length=50),
        ),
        migrations.AlterField(
            model_name='perfilatleta',
            name='vezes_treina',
            field=models.CharField(choices=[('', '---Treinos por semana.---'), ('', '1.'), ('', '2.'), ('', '3.'), ('', '4.'), ('', '5.'), ('', '6.'), ('', '7.')], max_length=50),
        ),
    ]
