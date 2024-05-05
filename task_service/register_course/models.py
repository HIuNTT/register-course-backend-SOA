from django.db import models

# Create your models here.


class RegisterCourse(models.Model):
    task_id = models.CharField(max_length=255, primary_key=True, unique=True)
    state = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'register_course'