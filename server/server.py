from flask import Flask, Response, render_template
from webcam import WebcamFactory
from models.WebcamInfo import webcam_info_to_dict
from util.int import intTryParse
import socketio

sio = socketio.Server(async_mode="threading", cors_allowed_origins="*")
app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

webcam_factory = WebcamFactory()
webcam_dict = webcam_factory.create_all_webcams()


@app.route("/")
def index():
    # For debugging
    return render_template("index.html")


@app.route("/webcams")
def list_webcams():
    return list(webcam_dict.keys())


@app.route("/webcams/<webcam_index>/info")
def webcam_info(webcam_index):
    index, isInt = intTryParse(webcam_index)
    if not isInt or index not in webcam_dict:
        return "Invalid webcam id", 400

    webcam = webcam_dict[index]
    return webcam_info_to_dict(webcam.get_stats())


@app.route("/webcams/<webcam_index>/stream/")
def video_feed(webcam_index):
    index, isInt = intTryParse(webcam_index)
    if not isInt or index not in webcam_dict:
        return "Invalid webcam id", 400

    webcam = webcam_dict[index]
    return Response(
        webcam.next_frame(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@sio.on("message")
def things(arg, data):
    print(data)


@sio.on("brightness")
def change_brightness(arg, data):
    webcam_index = data["webcam"]
    if webcam_index not in webcam_dict:
        return

    brightness = data["brightness"]
    brightness = min(brightness, 1)
    brightness = max(brightness, -1)
    webcam = webcam_dict[webcam_index]
    webcam.set_brightness(brightness)


@sio.on("saturation")
def change_brightness(arg, data):
    webcam_index = data["webcam"]
    if webcam_index not in webcam_dict:
        return

    saturation = data["saturation"]
    saturation = min(saturation, 1)
    saturation = max(saturation, -1)
    webcam = webcam_dict[webcam_index]
    webcam.set_saturation(data["saturation"])


@sio.on("exposure")
def change_brightness(arg, data):
    webcam_index = data["webcam"]
    if webcam_index not in webcam_dict:
        return
    exposure = data["exposure"]
    exposure = min(exposure, 1)
    exposure = max(exposure, -1)
    webcam = webcam_dict[webcam_index]
    webcam.set_exposure(data["exposure"])


@sio.on("hue")
def change_brightness(arg, data):
    webcam_index = data["webcam"]
    if webcam_index not in webcam_dict:
        return
    hue = data["hue"]
    hue = min(hue, 1)
    hue = max(hue, -1)
    webcam = webcam_dict[webcam_index]
    webcam.set_hue(data["hue"])


@sio.on("set_play_status")
def set_play_status(arg, data):
    webcam_index = data["webcam"]
    if webcam_index not in webcam_dict:
        return

    isPlaying = data["play"]
    webcam = webcam_dict[webcam_index]
    if isPlaying:
        webcam.play()
    else:
        webcam.pause()
