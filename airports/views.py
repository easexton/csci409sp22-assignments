from django.http import HttpResponse
from .models import Airport

def index(request):
    airports = Airport.objects.all()
    # Create a displayable string.
    airport_list = ', '.join([a.airport_code for a in airports])
    return HttpResponse('Showing all airports: ' + airport_list)


def airport_info(request, airport_code):
    # Fetch the airport by a certain code
    airport = Airport.objects.get(airport_code=airport_code)
    # Display the airport name and code
    return HttpResponse('Showing info for airport: ' + airport.name + " - " + airport.airport_code)
