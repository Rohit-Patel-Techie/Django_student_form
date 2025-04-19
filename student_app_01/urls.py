from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_create, name='student_create'),
    path('test_view/', views.test_view, name = "test")
]