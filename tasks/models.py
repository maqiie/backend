# tasks/models.py
from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='Low')

    def __str__(self):
        return self.task
