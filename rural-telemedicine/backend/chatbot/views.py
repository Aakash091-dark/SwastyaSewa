from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def process_message(request):
    """
    Process an incoming chat message and return a reply.
    For demo purposes, this uses a simple rule-based response.
    """
    message = request.data.get('message', '')
    # Simple rule-based logic for demonstration.
    if "appointment" in message.lower():
        reply = "I can help you book an appointment. Please provide your details."
    elif "hello" in message.lower():
        reply = "Hello! How can I assist you today?"
    else:
        reply = "I'm sorry, I didn't understand that. Could you please rephrase?"
    return Response({"reply": reply})

