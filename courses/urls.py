from django.urls import path
from . import views


urlpatterns = [
    path("",views.list_course, name ="courses"),
    path("enroll/<int:group_id>",views.enrollment, name ="enroll"),
    path("course/<int:course_id>", views.details, name="details"),
    path("track/<int:track_id>", views.track_details, name="track_details"),

]