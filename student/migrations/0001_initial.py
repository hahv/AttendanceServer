# Generated by Django 2.2.7 on 2019-12-04 03:56

from django.db import migrations, models
import django.db.models.deletion
import student.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('full_name', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=50)),
                ('student_code', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('student_video_data', models.FileField(null=True, upload_to=student.models.Student.path_and_rename)),
            ],
        ),
        migrations.CreateModel(
            name='StudentImagesData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_data', models.FileField(null=True, upload_to=student.models.StudentImagesData.path_and_rename)),
                ('image_date_upload', models.DateTimeField(auto_now_add=True, null=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]