from __future__ import absolute_import, unicode_literals
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random

from .tasks import *

def index(request):
    add.delay(4, 4)
    return HttpResponse("Rango says hey there partner!")
