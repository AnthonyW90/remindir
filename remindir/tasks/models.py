from django.conf import settings
from django.db import models
from recurrence.fields import RecurrenceField


class TaskGroup(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    label = models.CharField(max_length=60)
    slug = models.SlugField(max_length=150, unique=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='taskgroups')
    recurrences = RecurrenceField()

    def __str__(self):
        return self.label


class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=255, blank=True, null=True)
    taskgroup = models.ForeignKey(
        TaskGroup, on_delete=models.CASCADE, related_name='tasks')
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'${self.group} ${self.content}'
