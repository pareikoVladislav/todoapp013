# Generated by Django 5.0.1 on 2024-02-01 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(limit_choices_to={'status': 1}, on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='test_models.task'),
        ),
    ]
