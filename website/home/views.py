from django.shortcuts import render, redirect
from .models import Student
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def staff_required(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(staff_required)
def student(request):
    students = Student.objects.all()
    return render(request, 'home/students.html', {'students': students})

    