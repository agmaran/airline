from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Flight, Passenger
from django.urls import reverse
# Create your views here.


def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)  # You could use either id or pk
    return render(request, "flights/flight.html", {
        "flight": flight,
        # We can do this because passengers is the related_name
        "passengers": flight.passengers.all(),
        # Exclude passengers that among their flights have this particular flight
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })


def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        # Adds a new row into a table of keeping track the passengers on that flight
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=[flight_id]))
