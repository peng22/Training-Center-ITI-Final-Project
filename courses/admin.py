from django.contrib import admin
from .models import Course , ClassGroup , Enrollment

admin.site.register(Course)
admin.site.register(ClassGroup)
admin.site.register(Enrollment)

