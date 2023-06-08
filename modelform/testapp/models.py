from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=20)
    rollno = models.IntegerField()
    marks = models.FloatField(max_length=20)
