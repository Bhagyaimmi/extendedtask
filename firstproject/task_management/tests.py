from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Project, Task
from firstapp.models import User

class TaskManagementAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        # Create a user
        self.user = User.objects.create(username="testuser", email="test@example.com", password="password")
        
        # Authenticate the user
        self.client.force_authenticate(user=self.user)
        
        # Create a project
        self.project = Project.objects.create(title="Test Project", description="Test Description", start_date="2024-05-27", end_date="2024-06-27", user=self.user)
        
        # Create tasks associated with the project
        self.task1 = Task.objects.create(title="Task 1", description="Task 1 Description", priority=1, deadline="2024-06-01", assigned_to=self.user, project=self.project)
        self.task2 = Task.objects.create(title="Task 2", description="Task 2 Description", priority=2, deadline="2024-06-15", assigned_to=self.user, project=self.project)
    
    def test_project_list_authenticated(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, 200)
       
    def test_project_list_unauthenticated(self):
        self.client.logout() 
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, 401)  
    def test_task_list_authenticated(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)
    def test_task_list_unauthenticated(self):
        self.client.logout() 
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 401)  