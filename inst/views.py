from django.shortcuts import render , HttpResponse
from .models import Instructor

# Create your views here.
def inst(request):
    instructors = Instructor.objects.all()
    context = {"instructors" : instructors }
    return render(request,"inst/instructor.html",context)