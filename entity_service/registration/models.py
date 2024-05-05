from django.db import models

from course.models import Course
from student.models import Student


# Create your models here.


class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'registrations'
        ordering = ['created_at']
