from typing import Any, Dict


class WebcamInfo:
    def __init__(self, width, height, fps, brightness, contrast, saturation, hue):
        self.width = width
        self.height = height
        self.fps = fps
        self.brightness = brightness
        self.contrast = contrast
        self.saturation = saturation
        self.hue = hue


def webcam_info_to_dict(webcam: WebcamInfo) -> Dict[str, Any]:
    return vars(webcam)
