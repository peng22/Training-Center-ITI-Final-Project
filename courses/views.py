from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Course ,Instructor ,ClassGroup
# Create your views here.

def list_course(request):
    courses = list(Course.objects.all())
    # instructors = list(Instructor.objects.all())
    context = {"mycourses" : courses}
    return render(request, 'courses/courses.html', context)


def details(request,course_id):
    course = get_object_or_404(Course, pk = course_id) 
    course_groups = course.classgroup_set.all()
    context = {"course_groups" : course_groups , "course" : course}
    return render(request,'courses/details.html', context)

def enrollment(request,group_id):
    #TODO add authention check before enroll
    student = request.user.student
    group = ClassGroup.objects.get(pk=group_id)
    group.students.add(student)
    return render(request,'courses/mycourses.html')
