from django.urls import path

from project import views


urlpatterns = [
    path('articles/', views.articles)
]
