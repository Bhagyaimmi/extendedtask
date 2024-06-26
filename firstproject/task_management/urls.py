from django.urls import path
from task_management import views
urlpatterns = [
    
    path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('tasks/', views.TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/assign/<int:user_id>/', views.TaskAssign.as_view(), name='task-assign'),
    path('users/<int:user_id>/tasks/', views.UserTasksList.as_view(), name='user-tasks'),   
    path('tasks/<int:pk>/status/', views.UpdateTaskStatus.as_view(), name='task-update-status'),  
    path('tasks/<int:pk>/priority/', views.TaskPriorityUpdate.as_view(), name='task-priority-update'),
    path('weather/', views.FetchWeather.as_view(), name='fetch-weather'),
    path('weather/history/', views.WeatherListView.as_view(), name='weather-history'),
]
