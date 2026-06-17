from django.shortcuts import render

# Create your views here.
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.shortcuts import get_object_or_404


class StudentListCreateAPIView(APIView):
    def get(self, request,*args,**kwargs):
        student = StudentModel.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    
    
    
    