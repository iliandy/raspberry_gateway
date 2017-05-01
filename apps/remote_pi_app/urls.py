from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^$", views.index),
    url(r"^users/login$", views.loginUser),
    url(r"^home$", views.home),
    url(r"^open_door$", views.openDoor),
    url(r"^close_door$", views.closeDoor),
]
