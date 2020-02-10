from django.contrib import admin
from django.urls import path
from .views import list_course, get_details, list_inst, inst_details

urlpatterns = [
    path('courses/', list_course ,name="courses"),
    path('courses/<int:course_id>', get_details, name="details"),
    path('instructors/', list_inst, name="instructors"),
    path('instructors/<int:inst_id>',inst_details, name="inst_details"),
]
