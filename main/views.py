  
import csv,io
import subprocess
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.http import *
from .models import *
from django.contrib import messages
from django.contrib.auth.models import auth,User
from django.template import Context, loader

# Create your views here.
def homepage(request):
    #code = request.POST['codevalue']
    #print(code)
    return render(request,'editor.html')

