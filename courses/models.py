from django.db import models
from inst.models import Instructor
from student.models import Student


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_hours = models.IntegerField()
    course_price = models.IntegerField(default=0)
    def __str__(self):
        return self.course_name

#course instance 
class ClassGroup(models.Model):
    class_Instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    strat_date = models.DateField()
    end_date = models.DateField()
    students = models.ManyToManyField(Student, through = 'Enrollment' )
    def __str__(self):
        return f"{self.course} class ID no: {self.id}"


class Enrollment(models.Model):
    student_enroll = models.ForeignKey(Student, on_delete=models.PROTECT)
    course_enroll = models.ForeignKey(ClassGroup, on_delete= models.PROTECT)
    date_enroll = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"enrollment id : {self.id} "


