# Generated by Django 2.2.5 on 2020-06-12 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2020, 6, 12, 23, 23, 25, 192090)),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=40, unique=True, verbose_name='Name of Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='work_to_do',
            field=models.TextField(max_length=200, verbose_name='Assign Some Work'),
        ),
    ]