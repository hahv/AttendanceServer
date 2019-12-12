# Generated by Django 2.2.7 on 2019-12-12 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('course', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, to='student.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher.Teacher'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='schedule_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Schedule'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
    ]