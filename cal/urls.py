from django.urls import path
from . import views


urlpatterns = [
    path("student/profile/cal",views.CalendarView.as_view(), name ="calendar"),
]