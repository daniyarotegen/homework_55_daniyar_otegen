from django.db import models
from django.db.models import TextChoices


class StatusChoice(TextChoices):
    NEW = 'NEW', 'new'
    IN_PROCESS = 'IN_PROCESS', 'in process'
    COMPLETED = 'COMPLETED', 'completed'


class Task(models.Model):
    description = models.TextField(max_length=200, null=False, blank=False, verbose_name='description')
    details = models.TextField(max_length=2000, null=True, blank=True, verbose_name='detailed description')
    status = models.CharField(
        max_length=20, choices=StatusChoice.choices, default=StatusChoice.NEW, verbose_name='status'
    )
    completion_date = models.DateField(null=True, blank=True, verbose_name='completion date')

    def __str__(self):
        return f'{self.description} = {self.status}'
