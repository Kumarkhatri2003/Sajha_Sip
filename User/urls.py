from django.urls import path

from . import views


urlpatterns = [
    path('',views.checking,name='checking')
]
