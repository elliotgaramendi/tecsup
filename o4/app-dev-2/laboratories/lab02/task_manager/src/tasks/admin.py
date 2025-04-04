from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'status', 'due_date', 'created_date')
    list_filter = ('status', 'priority')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_date'
