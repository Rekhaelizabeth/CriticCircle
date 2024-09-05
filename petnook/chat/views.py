from django.shortcuts import render

def chatroom(request):
    return render(request, 'chatroom.html')

def room(request, room_name):
    return render(request, 'room.html', {'room_name': room_name})

from django.shortcuts import render, get_object_or_404
from .models import ChatRoom, Message

def chat_room(request, room_name):
    room = get_object_or_404(ChatRoom, name=room_name)
    messages = Message.objects.filter(room=room).order_by('timestamp')
    return render(request, 'chat/room.html', {'room': room, 'messages': messages})

