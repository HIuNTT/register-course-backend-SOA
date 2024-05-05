from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Student
from .serializers import StudentRegisSerializer


# Create your views here.


class RegisterStudentAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentRegisSerializer
    permission_classes = [permissions.AllowAny]