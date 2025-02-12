from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
import uuid

@api_view(['GET'])
def generate_video_room(request):
    """
    Generate a unique video room URL for a scheduled consultation.
    """
    room_id = str(uuid.uuid4())
    room_url = f"https://meet.jit.si/{room_id}"
    return Response({"room_url": room_url})

@api_view(['GET'])
def emergency_video(request):
    """
    Generate a fixed emergency video room URL for immediate connection.
    """
    # For demo purposes, we can use a fixed room name for emergencies.
    emergency_room = "emergency-room"
    room_url = f"https://meet.jit.si/{emergency_room}"
    return Response({"room_url": room_url})

