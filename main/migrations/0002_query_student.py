# Generated by Django 3.1.6 on 2021-02-11 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='student.student'),
        ),
    ]
