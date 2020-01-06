from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    session['user'] = "max"
    return render_template('index.html',name="gitik")

@socketio.on('join_room')
def join_room(message):
    print(message)
    print(session['user'] == "ss")
    ar = ["max","linux","kuroth","ash","may","misty","mitsuo","panko","bubi","payan","sumire"]
    socketio.emit('join_room_ans',{'name':ar})

@socketio.on('send')
def sd(message):
    print(message)
    if message['name'] == "password":
        socketio.emit('sd',{'name':session['user']})
    else:
        socketio.emit('sd',{'name':"wrong password"})


@socketio.on('event')
def event(message):
    print(message)
    socketio.emit('event_show',{'event':"this is an event"})

if __name__ == '__main__':
    socketio.run(app,port=8000,debug=True)