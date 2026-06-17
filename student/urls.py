from django.urls import path
from .views import StudentListCreateAPIView
from .models import StudentModel
from .serializers import StudentSerializer


urlpatterns = [
    path('student/', StudentListCreateAPIView.as_view()),
]