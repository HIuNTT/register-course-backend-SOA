from django.db import models

from subject.models import Subject

# Create your models here.


class Course(models.Model):
    group = models.IntegerField()
    max_slots = models.IntegerField()
    rest_slots = models.IntegerField()
    day = models.CharField(max_length=255)
    first_period = models.IntegerField()
    number_period = models.IntegerField()
    room = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    week = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'courses'
        ordering = ['group']



