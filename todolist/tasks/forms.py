from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    assigned_to = forms.ModelChoiceField(queryset=User.objects.all())
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'due_date', 'status', 'tag', 'priority']

        widgets = {
            'due_date': forms.DateInput(attrs ={'type': 'date', 'value': f'{timezone.now().date()}'}) 
        }
    
    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < timezone.now().date():
            raise ValidationError("La fecha de vencimiento no puede ser en el pasado.")
        return due_date