from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50)  # Nombre de la etiqueta

    def __str__(self):
        return self.name

class Priority(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name   

class Task(models.Model):
    STATUS_CHOICES = (
        ('P', 'Pendiente'),  # Estado Pendiente
        ('E', 'En progreso'),  # Estado En Progreso
        ('C', 'Completada'),  # Estado Completada
    )

    title = models.CharField(max_length=100)  # Título de la tarea
    description = models.TextField()  # Descripción de la tarea
    due_date = models.DateField()  # Fecha de vencimiento de la tarea
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')  # Estado de la tarea
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)  # Etiqueta asociada a la tarea
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks') #Usuario al cual se le asigna la tarea
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks') # Usuario que crea la tarea
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.title
    

 
