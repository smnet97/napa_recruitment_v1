# Generated by Django 3.1.6 on 2021-03-18 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_smsattempt_smscode'),
        ('student', '0008_auto_20210318_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='filters',
            field=models.ManyToManyField(blank=True, to='main.FilterValues'),
        ),
    ]
