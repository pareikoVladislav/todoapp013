# Generated by Django 5.0.1 on 2024-01-29 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_models', '0004_alter_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
