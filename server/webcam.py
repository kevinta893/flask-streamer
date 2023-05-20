import cv2

video = cv2.VideoCapture(0)

def next_frame():
    while True:
        success, frame = video.read() 
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def cleanup():
    # Cleanup webcam resources
    video.release()


