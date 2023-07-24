import json
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from elevators.dbhelper import checkElevatorWorking

from elevators.serializers import ElevatorSerializer
from .models import Elevator

# Create your views here.

def home(request):
    return HttpResponse("Success")


class ElevatorViewSet(viewsets.ViewSet):
    
    def list(self, request):
        elevators = Elevator.objects.all()
        serializedElevators = ElevatorSerializer(elevators, many=True)
        return Response(serializedElevators.data)
    
    def create(self, request):
        data = json.loads(request.body)
        name = data.get('name')
        floors = data.get('floors')
        currentFloor = data.get('current_floor',0)
        nextFloor = data.get('next_floor',1)
        newElevator = Elevator(name= name, floors=floors, currentFloor=currentFloor, nextFloor=nextFloor)
        newElevator.save()

        return HttpResponse("SUCCESS")



    def retrieve(self, request, id):
        elevatorData = Elevator.objects.get(id=id)
        serializedElevator = ElevatorSerializer(elevatorData)
        return Response(serializedElevator.data)

    def updateLiftCondition(self,request):
        data = json.loads(request.body)
        liftId = data.get('liftid')
        isWorking = data.get('is_working')
        isUnderMaintainance = data.get('is_under_maintainance')
        if isWorking and isUnderMaintainance:
            return HttpResponse("Elevator can not we working and under maintainance together")
        Elevator.objects.filter(id=liftId).update(isWorking=isWorking, isUnderMaintenance=isUnderMaintainance)

        return HttpResponse("Lift Status updated successfully")



class ElevatorNavigation(viewsets.ViewSet):
    def navigate(self, request):
        data = json.loads(request.body)
        liftId = data.get('liftId')
        requestedFloor = data.get('floor')
        if checkElevatorWorking(liftId):
            Elevator.objects.filter(id=liftId).update(currentFloor=requestedFloor)
            return HttpResponse("SUCCESS")
        return HttpResponse("Elevator is either not working or is under maintainance")
