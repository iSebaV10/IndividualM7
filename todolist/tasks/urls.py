from django.urls import path, include
from . import views
from tasks.views import index_view
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

#app_name = 'tasks'

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/create/<int:id>', views.task_create, name='task_create'),
    path('task/edit/<int:task_id>/', views.task_edit, name='task_edit'),
    path('task/delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('tasks_list/', views.task_list, name='tasks_list'),
    path('statics/',views.task_statistics, name='task_statics'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
