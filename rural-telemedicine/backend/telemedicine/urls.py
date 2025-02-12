from django.urls import path
from .views import generate_video_room, emergency_video

urlpatterns = [
    path('room/', generate_video_room, name='generate_video_room'),
    path('emergency/', emergency_video, name='emergency_video'),
]
