from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from ITI.models import Course, Instructor
# Create your views here.

course_data =list(Course.objects.all())
##[<>,<>,<>]
instructor_data=list(Instructor.objects.all())

mydiction = {
    "mycourses": course_data
}
myinst = {
    "instructors": instructor_data
}





def list_course(request):
    return render(request, 'ITI/index.html', context=mydiction)

def get_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {"course" : course}
    return render(request,'ITI/details.html', context)

def list_inst(request):
    return render(request, 'ITI/inst.html', context=myinst)

def inst_details(request, inst_id):
    instructor = get_object_or_404(Instructor, pk=inst_id)
    context = {"instructor" : instructor}
    return render(request,'ITI/inst_details.html', context)








    # return render(request, 'ITI/details.html', context=sent_course)