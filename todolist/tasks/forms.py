from django.core.exceptions import ValidationError
from django.utils import timezone
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'tag']

        widgets = {
            'due_date': forms.DateInput(attrs ={'type': 'date', 'value': f'{timezone.now().date()}'}) 
        }
    
    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < timezone.now().date():
            raise ValidationError("La fecha de vencimiento no puede ser en el pasado.")
        return due_date