from django.urls import path, include

from . import views

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('employees/', views.EmployeeListView.as_view(), name="employee_list"),
    path('teachers/', views.TeacherListView.as_view(), name="teacher_list"),
    path('admins/', views.AdminListView.as_view(), name="admin_list"),
    path('employee/<int:id>/', views.EmployeeInfoView.as_view(), name="employee_info"),
    path('user/logout/', views.LogoutAPIView.as_view(), name="logout")
]
