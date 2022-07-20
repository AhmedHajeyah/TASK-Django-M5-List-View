from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from .serializers import FlightSerializer, BookingSerializer



"""
Create a view that shows a list of Flights:
Complete it so that it displays the following fields for each flight:
id
destination
time
price
Create a URL with name flights-list for the above view and test it in Postman.
"""

class FlightListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class BookingListView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer