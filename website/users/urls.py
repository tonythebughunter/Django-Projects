from django.urls import path
from . import views
app_name = 'users'

urlpatterns = [
    path('login/', views.log, name='login'),
    path('register/', views.reg, name='register'),
    path('logout/', views.out, name='logout')
]