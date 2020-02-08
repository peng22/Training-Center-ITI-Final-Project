from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('studentreg/', views.studentReg ,name='studentreg'),
    path('student/profile/courses', views.mycourses , name='studentcourses'),
    path('login/', auth_views.LoginView.as_view(template_name='student/login.html' ) ,name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='student/logout.html') ,name='logout') ,

]

