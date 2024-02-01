from django.db import models

from apps.test_models.db_helpers import generate_default_title


class Category(models.Model):
    name = models.CharField(
        max_length=25,
        unique=True
    )


class Status(models.Model):
    name = models.CharField(
        max_length=25,
        unique=True
    )


class Task(models.Model):
    title = models.CharField(
        max_length=75,
        verbose_name='НАЗВАНИЕ ЗАДАЧИ',
        default=generate_default_title,
        unique=True,
    )
    description = models.CharField(
        max_length=1000,
        default='Здесь может быть ваше описание к задаче',
        unique_for_date='date_started',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    date_started = models.DateTimeField(
        help_text='ДАТА, КОГДА ЗАДАЧА БЫЛА СОЗДАНА',
        auto_now_add=True,
    )
    deadline = models.DateTimeField()
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        auto_now=True,
    )
