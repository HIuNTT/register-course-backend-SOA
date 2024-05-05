import time

from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import CourseSerializer
from subject.models import Subject


# Create your views here.

class CourseViewSet(APIView):
    # authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, id):
        subject = Subject.objects.get(id=id)
        courses = subject.courses.all()
        serializer = CourseSerializer(courses, many=True)
        time.sleep(3)
        return Response(serializer.data, status=status.HTTP_200_OK)

