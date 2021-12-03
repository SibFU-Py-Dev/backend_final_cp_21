from django.urls import path, include
from . import views


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('employee/<int:id>/', views.EmployeeInfoView.as_view(), name="employee_info"),
    path('user/logout/', views.LogoutAPIView.as_view(), name="logout")
]
