from django.shortcuts import render, redirect, HttpResponse
from .models import *




def index(request):

	return render(request, "remote_pi_app/index.html")