from django.urls import path

from . import views

urlpatterns = [
    path("hi", views.hi, name="hi"),
    path("", views.hello, name="hello"),
]