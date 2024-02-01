from django.contrib import admin
from apps.test_models.models import (
    Task,
    SubTask,
    Category,
    Status,
)


# admin.site.register(Task)
# admin.site.register(SubTask)
# admin.site.register(Category)
# admin.site.register(Status)
# admin.site.register(TestModel)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'status',
        'creator',
        'date_started',
        'deadline'
    ]
    list_filter = [
        'category',
        'status',
        'date_started'
    ]
    search_fields = ['title',]


@admin.register(SubTask)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'task',
        'status',
        'creator',
        'date_started',
        'deadline'
    ]
    list_filter = [
        'category',
        'status',
        'date_started',
        'deadline'
    ]
    search_fields = [
        'title',
    ]

    def up_title_register(self, request, queryset):
        for obj in queryset:
            obj.title = obj.title.upper()
            obj.save()

    up_title_register.short_description = 'Поднять регистр'

    def down_title_register(self, request, queryset):
        for obj in queryset:
            obj.title = obj.title.lower()
            obj.save()

    down_title_register.short_description = ' Опустить регистр'

    actions = [
        'up_title_register',
        'down_title_register'
    ]


@admin.register(Category)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Status)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ['name']
