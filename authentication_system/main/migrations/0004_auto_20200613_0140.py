# Generated by Django 2.2.5 on 2020-06-12 20:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200613_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2020, 6, 13, 1, 40, 1, 748906)),
        ),
    ]