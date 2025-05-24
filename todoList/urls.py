
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('api/', include('todo_api.urls')),
    path('admin/', admin.site.urls),
    path('', include("task.urls")),
    path('api/auth/', include('users.urls')),
]
