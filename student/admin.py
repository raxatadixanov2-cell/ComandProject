from django.contrib import admin

# Register your models here.
from .models import StudentModel



class Admin_Student(admin.ModelAdmin):
    list_display = ('name', 'surname', 'birthday', 'age', 'username', 'gender', 'email')

admin.site.register(StudentModel)