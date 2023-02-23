from django.contrib import admin
from todo.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'details', 'status', 'completion_date')
    list_filter = ('id', 'description', 'status', 'completion_date')
    search_fields = ('id', 'description')
    fields = ('id', 'description', 'details', 'status', 'completion_date')
    readonly_fields = ['id']


admin.site.register(Task, TaskAdmin)
