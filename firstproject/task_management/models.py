from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField()
    deadline = models.DateField()
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    def __str__(self):
        return self.title
