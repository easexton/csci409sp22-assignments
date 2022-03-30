from django.http import HttpResponse
from django.shortcuts import render
from .models import Airport

def index(request):
    airports = Airport.objects.all()
    # Place all airports into a context var
    context = {'airports': airports}
    return render(request, 'airports/index.html', context)


def airport_info(request, airport_code):
    # Fetch the airport by a certain code
    airport = Airport.objects.get(airport_code=airport_code)
    # Place airport into a context var
    context = {'airport': airport}
    return render(request, 'airports/airport.html', context)
