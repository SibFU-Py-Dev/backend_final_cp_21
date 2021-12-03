# Generated by Django 3.2.9 on 2021-12-03 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('verifiability', models.BooleanField()),
                ('experience', models.IntegerField()),
                ('in_course', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UserTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline', models.DateTimeField()),
                ('perfect_deadline', models.DateTimeField()),
                ('status', models.CharField(choices=[('S1', 'Подтверждено'), ('S2', 'Отклонено')], max_length=2)),
                ('estimation', models.SmallIntegerField()),
                ('description', models.TextField()),
                ('responsible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsible_tasks', related_query_name='responsible_task', to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tasks', related_query_name='user_task', to='tasks.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tasks', related_query_name='user_task', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
