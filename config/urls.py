from django.contrib import admin
from django.urls import path, include
from tasks import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.dashboard, name='dashboard'), 
    path('create/', views.create_task, name='create_task'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('categories/', views.categories_list, name='categories'),
    path('priorities/', views.priorities_list, name='priorities'),
    path('subtasks/', views.subtasks_list, name='subtasks'),
    path('notes/', views.notes_list, name='notes'),
]