from django.shortcuts import render
from home.models import Student
from posts.models import post
from django.http import JsonResponse
# Create your views here.

def studentApiview(request):
    student = Student.objects.all()
    student_list = list(student.values())
    return JsonResponse(student_list, safe=False)

def postApiView(request):
    posts = post.objects.all()
    posts_list = list(posts.values())
    return JsonResponse(posts_list, safe=False)
