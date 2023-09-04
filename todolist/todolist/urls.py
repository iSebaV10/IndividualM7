from django.contrib import admin
from django.urls import path, include

'''
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from tasks.views import index_view
from tasks import views
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
]
