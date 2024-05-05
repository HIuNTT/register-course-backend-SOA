from django.db import models

# Create your models here.


class Subject(models.Model):
    subject_id = models.CharField(max_length=255, unique=True)
    name = models.TextField()
    credit = models.IntegerField()

    class Meta:
        db_table = 'subjects'
        ordering = ['subject_id']

    def __str__(self):
        return self.name
