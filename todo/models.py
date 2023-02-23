from django.db import models


class Task(models.Model):
    NEW = 'new'
    COMPLETED = 'completed'
    IN_PROCESS = 'in process'
    STATUS_CHOICES = [
        (NEW, 'New'),
        (COMPLETED, 'Completed'),
        (IN_PROCESS, 'In Process'),
    ]

    description = models.TextField(max_length=200, null=False, blank=False, verbose_name='description')
    details = models.TextField(max_length=2000, null=True, blank=True, verbose_name='detailed description')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NEW, verbose_name='status')
    completion_date = models.DateField(null=True, blank=True, verbose_name='completion time')

    def __str__(self):
        return f'{self.description} = {self.status}'
