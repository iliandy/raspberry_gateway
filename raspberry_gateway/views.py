# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
# from gpio_func import *

# helper function to get current user id
def current_user(request):
    return User.objects.get(id = request.session["user_id"])


def index(request):
    print "-= Reached / (index.html) =-"
    return render(request, "raspberry_gateway/index.html")


def loginUser(request):
    print "-= Reached /users/login (redirect to gateway.html) =-"
    if request.method != "POST":
        return redirect("/")

    # validate login via validateUserLog from models.py
    check = User.objects.validateUserLog(request.POST)
    if check["pass"] is False:
        messages.error(request, check["errors"])
        return redirect("/")

    # valid email, password for login, store user id to session, go to gateway.html
    request.session["user_id"] = check["user"].id
    return redirect("/gateway")

def gateway(request):
    print "-= Reached /gateway (gateway.html) =-"
    if "door_closed" not in request.session:
        request.session["door_closed"] = True

    print request.session.items()
    data = {
        "user": current_user(request),
        "door_closed": request.session["door_closed"]
    }
    return render(request, "raspberry_gateway/gateway.html", data)

def operateDoor(request):
    print "-= Reached /operate_door (redirect to gateway.html) =-"

    if request.session["door_closed"]:
        request.session["door_closed"] = False
        # toggleSwitch()
        messages.info(request, "Garage door opening...")

    elif request.session["door_closed"] is False:
        request.session["door_closed"] = True
        # toggleSwitch()
        messages.info(request, "Garage door closing...")

    return redirect("/gateway")

def logoutUser(request):
    print "-= Reached /users/logout (redirect to /) =-"
    request.session["door_closed"] = True
    # toggleSwitch()
    request.session.clear()
    return redirect("/")
