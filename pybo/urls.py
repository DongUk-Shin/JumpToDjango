#path('pybo/', include('pybo.urls')) 

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
]