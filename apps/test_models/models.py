from django.db import models
from django.contrib.auth.models import User

from apps.test_models.db_helpers import (
    generate_default_title
)


def get_first_status():
    return Status.objects.first()


class TestModel(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'TestModel'
        verbose_name_plural = 'Test-Models'


class Category(models.Model):
    name = models.CharField(
        max_length=25,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Status(models.Model):
    name = models.CharField(
        max_length=25,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Task(models.Model):
    title = models.CharField(
        max_length=75,
        verbose_name='TASK NAME',
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
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    date_started = models.DateTimeField(
        help_text='ДАТА, КОГДА ЗАДАЧА БЫЛА СОЗДАНА',
        auto_now_add=True,
    )
    deadline = models.DateTimeField()
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.title[:8]}..."

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['date_started']
        unique_together = ('category', 'status', 'description')
        get_latest_by = 'date_started'

    # status = Status.objects.latest()
#
# Task1 -> deadline -> Task3 -> status -> Task1
# Task2 -> deadline -> Task1 -> status -> Task3
# Task3 -> deadline -> Task2 -> status -> Task4
# Task4 -> deadline -> Task4 -> status -> Task2


class SubTask(models.Model):
    title = models.CharField(
        max_length=75
    )
    description = models.TextField(
        max_length=700,
        blank=True,
        null=True
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='subtasks',
        limit_choices_to={
            "status": 1,
        }
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.SET(get_first_status),
        null=True,
        blank=True
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    date_started = models.DateTimeField(
        auto_now_add=True,
    )
    deadline = models.DateTimeField()
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.title[:8]}..."

    class Meta:
        verbose_name = 'SubTask'
        verbose_name_plural = 'SubTasks'
