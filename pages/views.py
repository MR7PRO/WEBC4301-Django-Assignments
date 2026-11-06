
from datetime import date
from django.shortcuts import render, redirect
from .models import StudentProfile, Student
from .forms import StudentForm


def index(request):
    context = {
        'first_name': 'ayham',
        'last_name': 'El Hour',
        'student_id': '120221684',
        'address': 'gaza, palestine',
        'email': 'ayham.a.alhour@gmail.com',
        'date_of_birth': date(2003, 5, 13),
    }

    return render(request, 'pages/index.html', context)


def home(request):
    students = StudentProfile.objects.all()

    context = {
        'students': students
    }
    return render(request, 'pages/home.html', context)


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)

        # هان بنتأكد من البيانات قبل ما نحفظها
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'pages/add_student.html', {
        'form': form
    })


def student_list(request):
    students = Student.objects.all()

    return render(request, 'pages/student_list.html', {
        'students': students
    })
