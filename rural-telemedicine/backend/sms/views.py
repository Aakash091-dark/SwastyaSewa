from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
from twilio.rest import Client

@api_view(['POST'])
def send_sms(request):
    """
    Send an SMS using Twilio.
    Expects 'phone' and 'message' in the request data.
    """
    phone = request.data.get('phone')
    message = request.data.get('message')
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_phone = os.getenv("TWILIO_PHONE_NUMBER")

    if not all([phone, message, account_sid, auth_token, twilio_phone]):
        return Response({"error": "Missing parameters or credentials."}, status=400)
    
    try:
        client = Client(account_sid, auth_token)
        sms = client.messages.create(
            body=message,
            from_=twilio_phone,
            to=phone
        )
        return Response({"status": "SMS sent", "sid": sms.sid})
    except Exception as e:
        return Response({"error": str(e)}, status=500)

