from django.urls import path
from . import views
urlpatterns = [
    path('student/', views.studentApiview),
    path('post/', views.postApiView)
]