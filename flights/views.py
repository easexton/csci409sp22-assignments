from django.http import HttpResponse
from .models import Flight # Import Flight model
from airports.models import Airport # Import airport model to get airport id and code
from django.shortcuts import render
from .forms import FlightForm

def index(request):
    form = FlightForm()
    return render(request, 'flights/index.html', {'form': form})

def search(request):
    form = FlightForm(request.POST)
    if form.is_valid():
        origin = Airport.objects.get(airport_code=form.cleaned_data['origin'])
        destination = Airport.objects.get(airport_code=form.cleaned_data['destination'])
        return render(request, 'flights/flight_search.html', {'origin': origin}, {'destination': destination})


def flight_search(request, origin, destination):
    origin = Airport.objects.get(airport_code=origin)
    destination = Airport.objects.get(airport_code=destination)
    # Code to select flights from the database
    flights = Flight.objects.get(origin, destination)
    flight_list = ', '.join([f.origin.airport_code + "->" + f.destination.airport_code + " Airline Code: " +
                             f.airline.airline_code for f in flights])
    return HttpResponse('Showing flights: ' + flight_list)


