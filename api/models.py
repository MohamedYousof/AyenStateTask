from django.db import models

TASK_STATES = [
    ('new', 'New'),
    ('in_progress', 'In Progress'),
    ('done', 'Done'),
]


class Task(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    state = models.CharField(max_length=11, choices=TASK_STATES, default='new')
    linked_task = models.IntegerField(null=True,  blank=True)

    def __str__(self):
        return self.title
