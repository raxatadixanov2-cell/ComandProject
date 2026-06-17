from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TeacherModel
from .serializers import TeacherSerializer

class TeacherCreateView(APIView):
    def post(self, request,*args,**kwargs):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors)


    
