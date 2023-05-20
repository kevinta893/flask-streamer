from flask import Flask, Response, current_app, render_template
from webcam import next_frame
import socketio

sio = socketio.Server(async_mode="threading", cors_allowed_origins='*')
app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(next_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

@sio.on('message')
def things(argthing, data):
    print(data)