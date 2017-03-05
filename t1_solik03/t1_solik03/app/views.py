"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Me

def home(request):
    user = Me.objects.all()[0]
    html = render(request,'app/home.html',{'user':a})
    return html

