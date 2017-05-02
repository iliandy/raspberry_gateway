# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# import re, bcrypt
# import time
# import RPi.GPIO as GPIO
# import re, bcrypt

# GPIO.setmode(GPIO.BOARD)
# pin = 11
# GPIO.setup(pin, GPIO.OUT)

class UserManager(models.Manager):
    def validateUserLog(self, post_data):
        # verify if email, password is blank
        if len(post_data["email"]) < 1 or len(post_data["password"]) < 1:
            return {"pass": False, "errors": "Login credentials can't be blank."}

        # verify email, password against db for valid user
        this_user = User.objects.filter(email = post_data["email"]).first()
        # if this_user and bcrypt.checkpw(post_data["password"].encode(), this_user.password.encode()):
        if this_user and post_data["password"] == this_user.password:
            return {"pass": True, "user": this_user}

        return {"pass": False, "errors": "Invalid login credentials."}

class User(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __str__(self):
        return "ID: {}, Name: {}, e-mail: {}, Password: {}".format(self.id, self.name, self.email, self.password)


def openDoor():
   GPIO.output(pin, True)

def closeDoor():
   GPIO.output(pin, False)
