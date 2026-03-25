from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Category, Priority, Task, Note, SubTask

@admin.register(Task)
class TaskAdmin(ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'priority', 'category', 'created_at')
    list_filter = ('status', 'priority', 'category', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(SubTask)
class SubTaskAdmin(ModelAdmin):
    list_display = ('title', 'status', 'parent_task_name', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')

    def parent_task_name(self, obj):
        return obj.parent_task.title
    parent_task_name.short_description = 'Parent Task'

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Priority)
class PriorityAdmin(ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Note)
class NoteAdmin(ModelAdmin):
    list_display = ('task', 'content', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content',)
    readonly_fields = ('created_at', 'updated_at')