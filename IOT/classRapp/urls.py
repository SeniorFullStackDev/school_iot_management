from django.urls import path
from .views import *
from .import views

urlpatterns = [
    path('', views.index, name='index1'),
   # path('/login', views.index, name='login')
]
