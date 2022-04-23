import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Places(models.Model):
    name            = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class BusChart(models.Model):
    fromP           = models.ForeignKey(Places, on_delete=models.CASCADE, related_name="fromPB")
    toP             = models.ForeignKey(Places, on_delete=models.CASCADE, related_name="toPB")
    departure       = models.TimeField()
    arival          = models.TimeField()
    adultcost       = models.FloatField()
    childcost       = models.FloatField()

    def __str__(self):
        return (self.fromP.name + " - " + self.toP.name)

class BusTrip(models.Model):
    ticket = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(BusChart, on_delete=models.CASCADE)
    adult = models.BigIntegerField()
    child = models.BigIntegerField()
    totalcost = models.FloatField()
    departureDate = models.DateField()
    payment = models.CharField(max_length=120)

    def __str__(self):
        return str(self.ticket) + " - " + self.payment  