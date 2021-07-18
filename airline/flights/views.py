from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Airport, Passenger


# Create your views here.


def index(request):
    return render(request, "flights/index.html", {"flights": Flight.objects.all()})


def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)

    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })


def book(request, flight_id):
    # for a post request, add a new flight
    if request.method == 'POST':
        # accessing the flight
        flight = Flight.objects.get(pk=flight_id)

        # finding the passenger id form the submitted form data
        # what does means is that the data about which passenger ID we want to register
        # on this flight is going to be passed in via a form with an input field whose
        # name is passenger.
        # the name on any particular input field dictates what name we get  is received
        # when a route like this book route is able to process the request from the user.

        passenger_id = int(request.POST["passenger"])

        # finding the passenger base on id
        passenger = Passenger.objects.get(pk=passenger_id)

        # add passenger to the flight
        passenger.flights.add(flight)

        # redirect page to the flight
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))


# def airport(request, airport_code):
#     airport = Airport.objects.get(pk=airport_code)
#     return render(request, "flights/airport.html", {
#         "airport": airport
#     })
