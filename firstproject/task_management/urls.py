from django.urls import path
from task_management import views
from .views import CreateUser, UserList
urlpatterns = [
    path('users/create/', CreateUser.as_view(), name='create-user'),
    path('createdusers/', UserList.as_view(), name='user-list'),
    path('projects/', views.ProjectListCreate.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectRetrieveUpdateDestroy.as_view(), name='project-detail'),
    path('tasks/', views.TaskListCreate.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroy.as_view(), name='task-detail'),
    path('tasks/<int:pk>/assign/<int:user_id>/', views.TaskAssign.as_view(), name='task-assign'),
    path('users/<int:user_id>/tasks/', views.UserTasksList.as_view(), name='user-tasks')    
]
