from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.index),
    url(r"^users/login$", views.loginUser),
    url(r"^home$", views.home),
    url(r"^users/logout$", views.logoutUser),
    url(r"^operate_door$", views.operateDoor),
]
