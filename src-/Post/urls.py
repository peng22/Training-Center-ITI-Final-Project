from django.conf.urls import url
from . import views

app_name='Post'

urlpatterns = [
    url(r'^$', views.all_posts,name='all_posts'),
    url(r'^(?P<id>\d+)$', views.post,name='post'),
    # path('comment/<int:id>/', views.comment, name='comment'),

    url(r'^create', views.create_post,name='create_post'),
    url(r'^(?P<id>\d+)/edit$', views.edit_post,name='edit_post'),
    url(r'^comment/(?P<id>\d+)$', views.comment,name='comment'),





]
