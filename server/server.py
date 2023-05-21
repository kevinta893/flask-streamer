from flask import Flask, Response, current_app, render_template
from webcam import Webcam, WebcamFactory
from models.WebcamInfo import webcam_info_to_dict
import socketio

sio = socketio.Server(async_mode="threading", cors_allowed_origins="*")
app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

webcam_factory = WebcamFactory()
webcam_dict = webcam_factory.create_all_webcams()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/webcams")
def list_webcams():
    return list(webcam_dict.keys())


@app.route("/webcams/<webcam_index>/info")
def webcam_info(webcam_index):
    index = int(webcam_index)
    if index not in webcam_dict:
        return "Invalid webcam id", 400

    webcam = webcam_dict[index]
    return webcam_info_to_dict(webcam.get_stats())


@app.route("/webcams/stream/<webcam_index>")
def video_feed(webcam_index):
    index = int(webcam_index)
    if index not in webcam_dict:
        return "Invalid webcam id", 400

    webcam = webcam_dict[index]
    return Response(
        webcam.next_frame(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@sio.on("message")
def things(argthing, data):
    print(data)
