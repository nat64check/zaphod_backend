# Generated by Django 2.0b1 on 2017-11-05 20:28

import django.db.models.deletion
import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('code', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='code')),
                ('level', models.PositiveSmallIntegerField(verbose_name='level')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('countries', django_countries.fields.CountryField(blank=True, max_length=746, multiple=True,
                                                                   verbose_name='countries')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                             to='world.Region', verbose_name='parent')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
