from django.shortcuts import render
from rest_framework import viewsets
from .models import Listing
from .serializers import ListingSerializer
from .models import Booking
from .serializers import BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# Milestone 5

from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer
from .tasks import send_booking_confirmation_email

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        send_booking_confirmation_email.delay(instance.id)
