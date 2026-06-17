from django.contrib import admin

# Register your models here.
from .models import TeacherModel



class Admin_Teacher(admin.ModelAdmin):
    list_display = ('name', 'surname', 'birthday', 'age', 'username', 'gender', 'email')

admin.site.register(TeacherModel)
