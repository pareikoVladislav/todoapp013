from django.db import models
from django.contrib.auth.models import User

from apps.test_models.db_helpers import (
    generate_default_title
)


class TestModel(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'TestModel'
        verbose_name_plural = 'Test-Models'
