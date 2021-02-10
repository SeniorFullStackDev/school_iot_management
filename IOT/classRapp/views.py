from django.shortcuts import render
from django.shortcuts import HttpResponse
from classRapp.models import Temp
from classRapp.models import Light
from classRapp.models import Humidity

# Create your views here.


def index(request):
     return render(request, '../templates/index1.html')


#def index1 (request):
#   return render(request, '../templates/login.html')


