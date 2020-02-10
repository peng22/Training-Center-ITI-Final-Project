from django.db import models

# Create your models here.
class Instructor(models.Model):
    instructor_name = models.CharField(max_length=20)
    def __str__(self):
        return self.instructor_name

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    start_date = models.DateTimeField('date published')
    course_price=models.IntegerField(default=0)
    course_instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    def __str__(self):
        return self.course_name





class Student(models.Model):
    student_name = models.CharField(max_length=200)
    def __str__(self):
        return self.student_name

class StudentCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE),
    student = models.ForeignKey(Student, on_delete=models.CASCADE),
    def __str__(self):
        return self.course_name
    def __str__(self):
        return self.student_name
