from django.urls import path
from . import views


urlpatterns = [
    path('tasks/<int:id>/', views.UserTasksView.as_view(), name="tasks_user"),
    path('task/', views.UserTaskCreateView.as_view(), name="create_task"),
]
