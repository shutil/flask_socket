var socket = io();
socket.emit('join_room', {
    name: "may"
});

socket.on('join_room_ans', (data) => {
    $('h2').text(data['name']);
    console.log(data['name']);
});

socket.emit('send', {
    name: "password"
});
socket.on('sd', (data) => {
    console.log(data);
});


socket.emit('event', {
    name: "gitik"
});
socket.on('event_show', (data) => {
    console.log(data);
});