from django.shortcuts import render
from .models import Student
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
@login_required
def index_view(request):
    return render(request, 'home/index.html')

def staff_required(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(staff_required)
def student_view(request):
    students = Student.objects.all()
    return render(request, 'home/students.html', {'students': students})