from django.shortcuts import render
from home.models import Student
from django.http import JsonResponse
# Create your views here.

def studentApiView(request):
    students = Student.objects.all()
    students_list = list(students.values())
    return JsonResponse(students_list, safe=False)