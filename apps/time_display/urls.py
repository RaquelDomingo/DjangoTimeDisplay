from django.conf.urls import url, include
from . import views           # This line is new!
  
urlpatterns = [
    url(r'^$', views.index),
    url(r'^time_display$', views.index),
     # This line has changed!
]