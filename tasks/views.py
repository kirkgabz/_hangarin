from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task, SubTask, Note, Category, Priority
from .forms import TaskForm, SubTaskForm, NoteForm
from django.db.models import Q, Count
from django.core.paginator import Paginator

@login_required
def dashboard(request):
    search_query = request.GET.get('search', '')
    tasks = Task.objects.all()
    
    if search_query:
        tasks = tasks.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    
    # Ensures your dashboard top-right metrics and category loadout actually work!
    top_categories = Category.objects.annotate(task_count=Count('task')).order_by('-task_count')[:3]
    
    context = {
        'pending_tasks': tasks.filter(status='Pending'),
        'in_progress_tasks': tasks.filter(status='In Progress'),
        'completed_tasks': tasks.filter(status='Completed'),
        'search_query': search_query,
        'top_categories': top_categories,
        'total_subtasks': SubTask.objects.count(),
        'total_notes': Note.objects.count(),
        'total_categories': Category.objects.count(),
        'total_priorities': Priority.objects.count(),
    }
    return render(request, 'home.html', context)

@login_required
def task_board(request):
    search_query = request.GET.get('search', '')
    category_id = request.GET.get('category', '')
    priority_id = request.GET.get('priority', '')
    
    tasks = Task.objects.all()
    
    if search_query:
        tasks = tasks.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    if category_id:
        tasks = tasks.filter(category_id=category_id)
    if priority_id:
        tasks = tasks.filter(priority_id=priority_id)

    pending_list = tasks.filter(status='Pending')
    in_progress_list = tasks.filter(status='In Progress')
    completed_list = tasks.filter(status='Completed')

    p_pending = Paginator(pending_list, 3)
    p_in_progress = Paginator(in_progress_list, 3)
    p_completed = Paginator(completed_list, 3)

    pending_tasks = p_pending.get_page(request.GET.get('pending_page'))
    in_progress_tasks = p_in_progress.get_page(request.GET.get('in_progress_page'))
    completed_tasks = p_completed.get_page(request.GET.get('completed_page'))

    context = {
        'pending_tasks': pending_tasks,
        'in_progress_tasks': in_progress_tasks,
        'completed_tasks': completed_tasks,
        'search_query': search_query,
    }
    return render(request, 'tasks.html', context)

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

    context = {
        'task': task,
        'subtasks': task.subtask_set.all(),
        'notes': task.note_set.all(),
        'subtask_form': SubTaskForm(),
        'note_form': NoteForm(),
    }
    return render(request, 'task_detail.html', context)

@login_required
def categories_list(request):
    categories_list = Category.objects.all()
    paginator = Paginator(categories_list, 8) 
    categories = paginator.get_page(request.GET.get('page'))
    return render(request, 'categories.html', {'categories': categories})

@login_required
def priorities_list(request):
    priorities_list = Priority.objects.all()
    paginator = Paginator(priorities_list, 8) 
    priorities = paginator.get_page(request.GET.get('page'))
    return render(request, 'priorities.html', {'priorities': priorities})

@login_required
def subtasks_list(request):
    subtask_list = SubTask.objects.all().order_by('-id')
    paginator = Paginator(subtask_list, 8) 
    subtasks = paginator.get_page(request.GET.get('page'))
    return render(request, 'subtasks.html', {'subtasks': subtasks})

@login_required
def notes_list(request):
    pending_list = Note.objects.filter(task__status='Pending').select_related('task').order_by('-created_at')
    in_progress_list = Note.objects.filter(task__status='In Progress').select_related('task').order_by('-created_at')
    completed_list = Note.objects.filter(task__status='Completed').select_related('task').order_by('-created_at')

    p_pending = Paginator(pending_list, 4)
    p_in_progress = Paginator(in_progress_list, 4)
    p_completed = Paginator(completed_list, 4)

    pending_notes = p_pending.get_page(request.GET.get('pending_page'))
    in_progress_notes = p_in_progress.get_page(request.GET.get('in_progress_page'))
    completed_notes = p_completed.get_page(request.GET.get('completed_page'))

    context = {
        'pending_notes': pending_notes,
        'in_progress_notes': in_progress_notes,
        'completed_notes': completed_notes,
    }
    return render(request, 'notes.html', context)