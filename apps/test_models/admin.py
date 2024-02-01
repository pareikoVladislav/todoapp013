from django.contrib import admin
from apps.test_models.models import (
    Task,
    Category,
    Status,
)

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Status)
