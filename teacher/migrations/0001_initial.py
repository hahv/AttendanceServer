# Generated by Django 2.2.7 on 2019-12-04 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('teacher_image', models.ImageField(null=True, upload_to='teachers/images')),
            ],
        ),
    ]
