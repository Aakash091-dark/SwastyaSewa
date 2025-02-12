from django.urls import path
from .views import process_message

urlpatterns = [
    path('message/', process_message, name='process_message'),
]
