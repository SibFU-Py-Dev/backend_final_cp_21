# Generated by Django 3.2.9 on 2021-12-03 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20211203_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='in_course',
        ),
    ]
