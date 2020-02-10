from django.shortcuts import render , HttpResponse ,get_object_or_404
from .models import Instructor

# Create your views here.
def inst(request):
    instructors = Instructor.objects.all()
    context = {"instructors" : instructors }
    return render(request,"inst/instructor.html",context)

def inst_details(request,inst_id):
    instructor = get_object_or_404(Instructor, pk = inst_id) 
    # course_groups = course.classgroup_set.all()
    context = {"instructor" : instructor}
    return render(request,'inst/inst-details.html', context)