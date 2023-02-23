from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets, DateInput
from todo.models import Task


class TaskForm(forms.Form):
    STATUS_CHOICES = (
        ('NEW', 'new'),
        ('COMPLETED', 'completed'),
        ('IN_PROCESS', 'in process')
    )
    description = forms.CharField(max_length=200, required=True, label='Description')
    details = forms.CharField(max_length=2000, required=True, label='Details', widget=widgets.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label='Status')
    completion_date = forms.DateField(
        required=False, label='Completion date', widget=DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Task
        fields = ['description', 'details', 'status', 'completion_date']

    def clean_title(self):
        description = self.cleaned_data.get('description')
        if len(description) < 2:
            raise ValidationError('Description must be longer than 2 symbols')
        return description
