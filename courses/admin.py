from django.contrib import admin
from .models import Course , ClassGroup , Enrollment ,Track
from .forms import ClassGroupForm



class ClassGroupAdmin(admin.ModelAdmin):
    form = ClassGroupForm
    

admin.site.register(Course)
admin.site.register(ClassGroup,ClassGroupAdmin)
admin.site.register(Enrollment)
admin.site.register(Track)
