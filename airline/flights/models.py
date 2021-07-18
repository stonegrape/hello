# from airline.flights.views import flight
# from airline import flights
from django.db import models
from django.shortcuts import render
# from django.db.models.query_utils import select_related_descend

# Create your models here.


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.id}:{self.origin} to {self.destination}"


class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(
        Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
