# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import *

# helper function to get current user id
def current_user(request):
    return User.objects.get(id = request.session["user_id"])


def index(request):
    print "-= Reached / (index.html) =-"
    print request.session.items()
    return render(request, "remote_pi_app/index.html")


def loginUser(request):
    print "-= Reached /users/login (redirect to home.html) =-"
    if request.method != "POST":
        return redirect("/")

    # validate login via validateUserLog from models.py
    check = User.objects.validateUserLog(request.POST)
    if check["pass"] is False:
        messages.error(request, check["errors"])
        return redirect("/")

    # valid email, password for login, store user id to session, go to home.html
    request.session["user_id"] = check["user"].id
    return redirect("/home")

def home(request):
    print "-= Reached /home (home.html) =-"
    if "door_closed" not in request.session:
        request.session["door_closed"] = True

    data = {
        "user": current_user(request),
        "door_closed": request.session["door_closed"]
    }
    return render(request, "remote_pi_app/home.html", data)

def operateDoor(request):
    print "-= Reached /operate_door (redirect to home.html) =-"

    if request.session["door_closed"]:
        request.session["door_closed"] = False
        openDoor()
        messages.success(request, "Garage door opening...")

    elif request.session["door_closed"] is False:
        request.session["door_closed"] = True
        closeDoor()
        messages.success(request, "Garage door closing...")

    return redirect("/home")

def logoutUser(request):
    print "-= Reached /users/logout (redirect to /) =-"
    request.session["door_closed"] = True
    # close_door func from GPIO .py
    request.session.clear()
    return redirect("/")
