from django.shortcuts import render, redirect
from .models import Student
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def staff_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            returnUrl = request.get_full_path()
            loginUrl = reverse('users:login')
            return redirect(f"{loginUrl}?{REDIRECT_FIELD_NAME}={returnUrl}")
        elif not user.is_staff:
            return HttpResponse('user not authorized to view', status=401)
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@staff_required
def student_view(request):
    students = Student.objects.all()
    return render(request, 'home/students.html', {'students': students})