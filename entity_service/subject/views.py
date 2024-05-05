from django.shortcuts import render
from rest_framework import viewsets, permissions, generics

from .models import Subject

from .serializers import SubjectSerializer


# Create your views here.

# Lấy ra danh sách môn học
class SubjectViewSet(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]