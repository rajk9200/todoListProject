

from django.urls import path
from . import views
from .views import dashboard

urlpatterns = [
    path('todo/', views.task_list),
    path('add/', views.task_add),
    path('tasks/', views.tasks),
    path('task_delete/<id>', views.task_delete),


    #API HOME
    path('home/', views.home),
    path('dashboard', views.dashboard),
]
