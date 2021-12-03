from django.urls import path
from . import views


urlpatterns = [
    path('user/tasks/', views.UserTasksView.as_view(), name="tasks_user"),
    path('task/', views.UserTaskCreateView.as_view(), name="create_task"),
]
