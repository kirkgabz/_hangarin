from django.contrib import admin
from django.urls import path, include
from tasks import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    
    # Existing Navigation
    path('', views.dashboard, name='dashboard'), 
    path('tasks/', views.task_board, name='tasks'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('categories/', views.categories_list, name='categories'),
    path('priorities/', views.priorities_list, name='priorities'),
    path('subtasks/', views.subtasks_list, name='subtasks'),
    path('notes/', views.notes_list, name='notes'),
    
    # Creation URLs
    path('create/', views.create_task, name='create_task'),
    path('subtasks/create/', views.create_subtask, name='create_subtask'),
    path('categories/create/', views.create_category, name='create_category'),
    path('priorities/create/', views.create_priority, name='create_priority'),
    path('notes/create/', views.create_note, name='create_note'),
]