# Generated by Django 2.0rc1 on 2017-11-19 18:53

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('measurements', '0003_schedule_ordering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instancerun',
            name='testrun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances',
                                    to='measurements.TestRun', verbose_name='test run'),
        ),
        migrations.AlterField(
            model_name='instancerunmessage',
            name='instancerun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages',
                                    to='measurements.InstanceRun'),
        ),
        migrations.AlterField(
            model_name='instancerunresult',
            name='instancerun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results',
                                    to='measurements.InstanceRun', verbose_name='instance'),
        ),
        migrations.AlterField(
            model_name='testrun',
            name='requested',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='requested'),
        ),
        migrations.AlterField(
            model_name='testrunmessage',
            name='testrun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages',
                                    to='measurements.TestRun'),
        ),
    ]