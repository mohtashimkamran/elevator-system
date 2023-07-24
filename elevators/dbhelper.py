from .models import Elevator

def checkElevatorWorking(id):
    elevatorObj = Elevator.objects.filter(id=id, isWorking=True, isUnderMaintenance=False)
    if elevatorObj:
        return True
    return False
    