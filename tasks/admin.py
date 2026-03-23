from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Category, Priority, Task, Note, SubTask

@admin.register(Task)
class TaskAdmin(ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'priority', 'category')
    list_filter = ('status', 'priority', 'category')
    search_fields = ('title', 'description')

@admin.register(SubTask)
class SubTaskAdmin(ModelAdmin):
    list_display = ('title', 'status', 'parent_task_name')
    list_filter = ('status',)
    search_fields = ('title',)

    def parent_task_name(self, obj):
        return obj.parent_task.title
    parent_task_name.short_description = 'Parent Task'

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Priority)
class PriorityAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Note)
class NoteAdmin(ModelAdmin):
    list_display = ('task', 'content', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content',)