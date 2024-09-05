from django.urls import path
from chat import views

urlpatterns = [
    path('chatroom/', views.chatroom, name='chatroom'),
    path('chat/<str:room_name>/', views.room, name='room'),
]
