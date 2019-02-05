# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Variablesmacroeconomicas',
            fields=[
                ('mes', models.DateField(primary_key=True, serialize=False)),
                ('pibreal', models.BigIntegerField(blank=True, null=True)),
                ('pibnominal', models.BigIntegerField()),
                ('tc', models.FloatField(blank=True, null=True)),
                ('factorestacionaidadexpo', models.FloatField(blank=True, null=True)),
                ('factorestacionaidadimpo', models.FloatField(blank=True, null=True)),
                ('estimacionexpo', models.FloatField(blank=True, null=True)),
                ('estimacionimpo', models.FloatField(blank=True, null=True)),
                ('estimacionexpodolares', models.FloatField(blank=True, null=True)),
                ('estimacionimpodolares', models.FloatField(blank=True, null=True)),
                ('estacionalidadpib', models.FloatField(blank=True, null=True)),
                ('ipimensualizado', models.FloatField(blank=True, null=True)),
                ('emaeso', models.FloatField(blank=True, null=True)),
                ('emaese', models.FloatField(blank=True, null=True)),
                ('ipcserie', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'variablesmacroeconomicas',
                'managed': True,
            },
        ),
    ]
