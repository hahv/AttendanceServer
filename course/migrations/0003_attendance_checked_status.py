# Generated by Django 2.2.7 on 2019-12-22 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_course_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='checked_status',
            field=models.BooleanField(default=False),
        ),
    ]
