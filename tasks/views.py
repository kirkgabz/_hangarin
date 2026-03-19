from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task, SubTask, Note, Category, Priority
from .forms import TaskForm, SubTaskForm, NoteForm
from django.db.models import Q

@login_required
def dashboard(request):
    search_query = request.GET.get('search', '')
    tasks = Task.objects.all()
    
    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    context = {
        'pending_tasks': tasks.filter(status='Pending'),
        'in_progress_tasks': tasks.filter(status='In Progress'),
        'completed_tasks': tasks.filter(status='Completed'),
        'search_query': search_query,
    }
    
    return render(request, 'home.html', context)

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
        
    return render(request, 'task_form.html', {'form': form})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        if 'add_subtask' in request.POST:
            subtask_form = SubTaskForm(request.POST)
            if subtask_form.is_valid():
                subtask = subtask_form.save(commit=False)
                subtask.parent_task = task
                subtask.save()
                return redirect('task_detail', pk=task.id)
                
        elif 'add_note' in request.POST:
            note_form = NoteForm(request.POST)
            if note_form.is_valid():
                note = note_form.save(commit=False)
                note.task = task
                note.save()
                return redirect('task_detail', pk=task.id)

    subtask_form = SubTaskForm()
    note_form = NoteForm()

    context = {
        'task': task,
        'subtasks': task.subtask_set.all(),
        'notes': task.note_set.all(),
        'subtask_form': subtask_form,
        'note_form': note_form,
    }
    return render(request, 'task_detail.html', context)

@login_required
def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

@login_required
def priorities_list(request):
    priorities = Priority.objects.all()
    return render(request, 'priorities.html', {'priorities': priorities})

@login_required
def subtasks_list(request):
    subtasks = SubTask.objects.all().order_by('-id')
    return render(request, 'subtasks.html', {'subtasks': subtasks})

@login_required
def notes_list(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes.html', {'notes': notes})