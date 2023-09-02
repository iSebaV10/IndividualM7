from django.urls import path
from . import views
from .views import CustomLoginView

app_name = 'tasks'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('tasks_list/', views.task_list, name='tasks_list'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/edit/<int:task_id>/', views.task_edit, name='task_edit'),
    path('task/delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('statics/',views.task_statistics, name='task_statics'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
