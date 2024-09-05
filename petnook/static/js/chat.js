// static/js/chat.js

document.addEventListener('DOMContentLoaded', function() {
    var roomName = document.querySelector('#room-name').textContent.trim();  // Ensure roomName is trimmed
    console.log('Connecting to WebSocket for room:', roomName);
    console.log('Room Name:ceckinggggggggggg');
    console.log('Room Name:', roomName);

    // Construct WebSocket URL
    var wsUrl = 'ws://' + window.location.host + '/ws/chat/' + roomName + '/';
    var ws = new WebSocket(wsUrl);

    ws.onopen = function() {
        console.log('WebSocket connection opened');
    };

    ws.onmessage = function(e) {
        console.log('Message received:', e.data);
        try {
            const data = JSON.parse(e.data);
            const message = data['message'];
            document.querySelector('#chat-log').value += (message + '\n');
        } catch (error) {
            console.error('Error parsing message:', error);
        }
    };

    ws.onerror = function(e) {
        console.error('WebSocket error:', e);
    };

    ws.onclose = function(e) {
        console.log('WebSocket connection closed:', e.reason);
    };

    document.querySelector('#chat-message-input').focus();
    document.querySelector('#chat-message-input').onkeyup = function(e) {
        if (e.keyCode === 13) {  // Enter key
            const messageInput = document.querySelector('#chat-message-input');
            const message = messageInput.value;
            console.log('Sending message:', message);
            ws.send(JSON.stringify({
                'message': message
            }));
            messageInput.value = '';  // Clear input field
        }
    };
});
