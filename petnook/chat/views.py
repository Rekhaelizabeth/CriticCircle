from django.shortcuts import render
from .models import ChatRoom, Message
from loginapp.models import CustomUser  # Import your custom user model if needed

def chatroom(request):
    if request.method == "POST":
        content = request.POST.get("content", "")
        user = request.user  # Assuming the user is authenticated

        if content:
            Message.objects.create(user=user, content=content)

    messages = Message.objects.all().order_by('-timestamp')
    return render(request, "chatroom.html", {"messages": messages})
