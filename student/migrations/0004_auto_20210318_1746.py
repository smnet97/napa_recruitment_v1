# Generated by Django 3.1.6 on 2021-03-18 17:46

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20210224_1443'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentprojects',
            options={'verbose_name': 'student project', 'verbose_name_plural': 'student projects'},
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='direction',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='skills',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_image',
            field=models.ImageField(blank=True, upload_to=student.models.convert_fn),
        ),
    ]
