from django.db import models

# Create your models here.
class Instructor(models.Model):
    instructor_name = models.CharField(max_length=20)
    instructor_Summary = models.CharField(max_length=200,default="Good Instructor")
    instructor_resume=models.FileField(upload_to="media/ITI/inst/resume/", max_length=100,default="No_resume")
    instructor_image=models.ImageField(upload_to="media/ITI/inst/", max_length=100,default="No_image")


    def __str__(self):
        return self.instructor_name

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    start_date = models.DateTimeField('date published')
    course_price=models.IntegerField(default=0)
    # course_review = models.CharField(max_length=200)
    course_cover=models.ImageField(upload_to="media/ITI/course/", max_length=100,default="No_image")
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
