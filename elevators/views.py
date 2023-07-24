import json
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from .models import Elevator

# Create your views here.

def home(request):
    return HttpResponse("Success")


class ElevatorViewSet(viewsets.ViewSet):
    
    def list(self, request):
        return HttpResponse("SUCCESS")
    
    def create(self, request):
        data = json.loads(request.body)
        name = data.get('name')
        floors = data.get('floors')
        newElevator = Elevator(name= name, floors=floors)
        newElevator.save()

        return HttpResponse("SUCCESS")



    def retrieve(self, request):
        return