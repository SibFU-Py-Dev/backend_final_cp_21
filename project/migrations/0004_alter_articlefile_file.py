# Generated by Django 3.2.9 on 2021-12-03 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20211204_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlefile',
            name='file',
            field=models.FileField(upload_to='articles/files/'),
        ),
    ]
