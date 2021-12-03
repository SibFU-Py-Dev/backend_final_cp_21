from django.urls import path
from . import views


urlpatterns = [
    path('task/user/<int:id>/', views.UserTasksView.as_view(), name="tasks_user"),
    path('task/', views.UserTaskCreateView.as_view(), name="create_task"),
]
