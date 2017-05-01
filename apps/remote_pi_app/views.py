from django.shortcuts import render, redirect, HttpResponse
from .models import *




def index(request):

	return render(request, "django_notes_app/index.html")