from django.urls import path
from .views import TeacherListCreateAPIView
from .models import TeacherModel
from .serializers import TeacherSerializer


urlpatterns = [
    path('teacher/', TeacherListCreateAPIView.as_view()),
    
]