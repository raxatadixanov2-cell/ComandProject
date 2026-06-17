from django.db import models

# Create your models here.
class TeacherModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthday = models.DateTimeField()
    age = models.IntegerField()
    username = models.CharField(max_length=100)
    a = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(max_length=100, choices=a)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username