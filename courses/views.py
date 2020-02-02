from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Course ,Instructor
# Create your views here.

def list_course(request):
    courses = list(Course.objects.all())
    # instructors = list(Instructor.objects.all())
    context = {"mycourses" : courses}
    return render(request, 'courses/courses.html', context)


def details(request,course_id):
    course = get_object_or_404(Course, pk = course_id) 
    context = {"course" : course}
    return render(request,'courses/details.html', context)


