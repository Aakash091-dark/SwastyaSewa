from django.shortcuts import render

from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting appointments.
    """
    queryset = Appointment.objects.all().order_by('-appointment_date')
    serializer_class = AppointmentSerializer

