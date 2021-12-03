# Generated by Django 3.2.9 on 2021-12-03 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20211203_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hint',
            name='hint',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hint_article', to='project.article'),
        ),
        migrations.AlterField(
            model_name='hint',
            name='hinted',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hinted_article', to='project.article'),
        ),
    ]