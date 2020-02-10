from django.urls import path
from . import views


urlpatterns = [
    path('',views.inst, name = "instuctor"),
    path("<int:inst_id>", views.inst_details, name="inst-details"),
    
]

