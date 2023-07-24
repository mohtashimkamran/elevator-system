from django.db import models

# Create your models here.
class Elevator(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    floors = models.IntegerField()
    

    def __str__(self):
        return self.name

