import time

from rest_framework import permissions, status, viewsets, generics
from rest_framework.response import Response

from .models import Registration
from .serializers import RegistrationSerializer
from course.models import Course


# Create your views here.

# Lấy danh sách đăng ký của sinh viên hiện tại
class RegistrationViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    def list(self, request, *args, **kwargs):
        queryset = Registration.objects.filter(student_id=request.user.id)
        serializer = RegistrationSerializer(queryset, many=True)
        time.sleep(3)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        student_id = request.user.id
        course_id = request.data.get('course')
        data = {
            'student': student_id,
            'course': course_id,
        }
        serializer = RegistrationSerializer(data=data)
        time.sleep(3)
        if serializer.is_valid():
            serializer.save()

            course = Course.objects.get(id=course_id)
            if course.rest_slots > 0:
                course.rest_slots -= 1
                course.save()
            else:
                return Response({'message': 'No slots available in this course'}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
