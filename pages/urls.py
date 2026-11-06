
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),

    # هان بنربط صفحات التعيين الجديد
    path('add-student/', views.add_student, name='add_student'),
    path('students/', views.student_list, name='student_list'),
]
