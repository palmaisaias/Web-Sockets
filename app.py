from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO()

socketio.init_app(app, cors_allowed_origins = '*')

messages = [] #storing messages in this list

@socketio.on('connect')
def handle_connect():
    print("You's LIVEEE")

@socketio.on('disconnect')
def handle_disconnect():
    print("You are NOT connected")

@socketio.on('message')
def handle_message(message):
    print(f"New Message: {message}")
    messages.append(message)
    socketio.emit('message',message) #is going to run its own event

@app.route("/")
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.debug = True
    socketio.run(app, debug=True)

