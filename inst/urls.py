from django.urls import path
from . import views


urlpatterns = [
    path('',views.inst, name = "instuctor"),
]

