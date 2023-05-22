import cv2
from models.WebcamInfo import WebcamInfo


class Webcam:
    def __init__(self, webcam_index):
        self.video = cv2.VideoCapture(webcam_index)
        self.exposure = 0
        self.saturation = 0
        self.brightness = 0
        self.hue = 0

    def next_frame(self):
        while True:
            success, frame = self.video.read()
            if not success:
                break
            else:
                ret, buffer = cv2.imencode(".jpg", frame)
                frame = buffer.tobytes()

            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")

    def get_stats(self):
        webcam = self.video
        return WebcamInfo(
            webcam.get(cv2.CAP_PROP_FRAME_WIDTH),
            webcam.get(cv2.CAP_PROP_FRAME_HEIGHT),
            webcam.get(cv2.CAP_PROP_FPS),
            webcam.get(cv2.CAP_PROP_BRIGHTNESS),
            webcam.get(cv2.CAP_PROP_CONTRAST),
            webcam.get(cv2.CAP_PROP_SATURATION),
            webcam.get(cv2.CAP_PROP_HUE),
        )

    def set_exposure(self, exposure):
        self.exposure = exposure
        self.video.set(cv2.CAP_PROP_EXPOSURE, exposure)

    def set_saturation(self, saturation):
        self.saturation = saturation
        self.video.set(cv2.CAP_PROP_SATURATION, saturation)

    def set_brightness(self, brightness):
        self.brightness = brightness
        self.video.set(cv2.CAP_PROP_BRIGHTNESS, brightness)

    def set_hue(self, hue):
        self.hue = hue
        self.video.set(cv2.CAP_PROP_HUE, hue)

    def cleanup(self):
        self.video.release()


class WebcamFactory:
    def __init__(self):
        index = 0
        webcams = []
        # Finds all available webcams on system, stops when runs out
        while True:
            cap = cv2.VideoCapture(index)
            if not cap.read()[0]:
                break
            else:
                webcams.append(index)
            cap.release()
            index += 1
        self.webcams = webcams

    def get_available_webcam_indicies(self):
        return self.webcams

    def create_webcam(self, index):
        if self.webcams.index(index) < 0:
            raise Exception(f"Invalid webcam index {index}")
        return Webcam(index)

    def create_all_webcams(self):
        webcam_instances = {}
        for webcam_index in self.webcams:
            webcam_instances[webcam_index] = Webcam(webcam_index)

        return webcam_instances
