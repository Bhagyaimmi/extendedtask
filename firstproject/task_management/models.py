from django.db import models
from firstapp.models import User

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title



class Task(models.Model):
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low')
    ]
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField( max_length=20,choices=PRIORITY_CHOICES, default='medium')
    deadline = models.DateField()
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return self.title
class Weather(models.Model):
    location = models.CharField(max_length=255)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.location} - {self.time}"
