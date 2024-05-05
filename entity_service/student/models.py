from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class Student(AbstractUser):
    date_birth = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    place_origin = models.TextField()
    address = models.TextField()
    training_level = models.CharField(max_length=255)
    is_owed = models.BooleanField(default=False)


    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'students'