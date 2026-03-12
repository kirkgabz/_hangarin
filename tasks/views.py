from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task, SubTask, Note
from .forms import TaskForm, SubTaskForm, NoteForm

@login_required
def dashboard(request):
    
    # Grouping the tasks into sections based on your document's status choices
    context = {
        'pending_tasks': Task.objects.filter(status='Pending'),
        'in_progress_tasks': Task.objects.filter(status='In Progress'),
        'completed_tasks': Task.objects.filter(status='Completed'),
    }
    return render(request, 'task_list.html', context)

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard') # Redirect back to the board after saving
    else:
        form = TaskForm()
        
    return render(request, 'task_form.html', {'form': form})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        # Did they click the "Add Subtask" button?
        if 'add_subtask' in request.POST:
            subtask_form = SubTaskForm(request.POST)
            if subtask_form.is_valid():
                subtask = subtask_form.save(commit=False) # Pause before saving to DB
                subtask.parent_task = task # Link it to the current task
                subtask.save() # Now save it
                return redirect('task_detail', pk=task.id)
                
        # Did they click the "Add Note" button?
        elif 'add_note' in request.POST:
            note_form = NoteForm(request.POST)
            if note_form.is_valid():
                note = note_form.save(commit=False) # Pause before saving to DB
                note.task = task # Link it to the current task
                note.save() # Now save it
                return redirect('task_detail', pk=task.id)

    # If it's just a normal page load (GET request), create blank forms
    subtask_form = SubTaskForm()
    note_form = NoteForm()

    context = {
        'task': task,
        'subtasks': task.subtask_set.all(), # Grab all subtasks linked to this task
        'notes': task.note_set.all(),       # Grab all notes linked to this task
        'subtask_form': subtask_form,
        'note_form': note_form,
    }
    return render(request, 'task_detail.html', context)