from django.contrib import admin
from .models import Student

class adminStud(admin.ModelAdmin):
    list_display = ('name', 'feeBal')

# Register your models here.
admin.site.register(Student, adminStud)