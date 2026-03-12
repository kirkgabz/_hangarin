from django import forms
from .models import Task, SubTask, Note

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'status', 'category', 'priority']
        
        # This applies Bootstrap styling directly to the Django form inputs
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task title...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'deadline': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
        }
class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ['title', 'status'] 
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'What needs to be done?'}),
            'status': forms.Select(attrs={'class': 'form-select form-select-sm'}),
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 2, 'placeholder': 'Jot down a quick note...'}),
        }