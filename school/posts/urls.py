from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('posts/', views.postView, name='post')
]