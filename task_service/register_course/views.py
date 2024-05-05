import requests
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import RegisterCourse
from .serializers import StateSerializer


# Create your views here.


class InitializationTask(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        task, created = RegisterCourse.objects.get_or_create(task_id='DKH')
        task.state = 'Initiatizing list subjects'
        task.save()

        headers = {'Authorization': request.headers.get('Authorization')}

        # Lấy danh sách môn học
        subjects = requests.get('http://127.0.0.1:8000/subject/', headers=headers).json()

        # Lấy danh sách lớp học phần của từng môn học
        for subject in subjects:
            task.state = 'Initiatizing list courses of subject ' + subject.get('subject_id')
            task.save()
            subject['courses'] = requests.get('http://127.0.0.1:8000/subject/{}/course/'.format(int(subject.get('id'))), headers=headers).json()

        task.state = 'Retrieving current student registration information'
        task.save()

        registrations = requests.get('http://127.0.0.1:8000/registration/', headers=headers).json()

        task.state = 'Completed'
        task.save()

        return Response({'classes': subjects, 'registration information': registrations}, status=status.HTTP_200_OK)


class CurrentStateTask(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):
        state = RegisterCourse.objects.get(task_id=id)
        serializer = StateSerializer(state)
        return Response(serializer.data, status=status.HTTP_200_OK)