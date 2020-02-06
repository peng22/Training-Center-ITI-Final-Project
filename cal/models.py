from django.db import models
from courses.models import ClassGroup

# Create your models here.
class Session(models.Model):
    course = models.ForeignKey(ClassGroup,on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
