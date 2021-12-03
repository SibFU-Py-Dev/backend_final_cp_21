# Generated by Django 3.2.9 on 2021-12-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.CharField(choices=[('ST', 'Новый сотрудник'), ('TC', 'Наставник'), ('AD', 'Руководитель проекта')], default='ST', max_length=2, verbose_name='Роль'),
        ),
    ]
