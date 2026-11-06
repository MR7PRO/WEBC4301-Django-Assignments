
from django.contrib import admin
from .models import StudentProfile, Student

# هان بنسجل الجدولين عشان يظهروا في لوحة الإدارة
admin.site.register(StudentProfile)
admin.site.register(Student)
