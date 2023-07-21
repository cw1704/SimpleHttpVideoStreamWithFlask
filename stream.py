from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# HHD-960-540,HDV-1280-720
def setCam(id):
    camera = cv2.VideoCapture(id)
    camera.set(cv2.CAP_PROP_SETTINGS,0.0); 
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640) #960
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 360) #540
    camera.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
    camera.set(cv2.CAP_PROP_FPS,60)
    return camera

cap = setCam(0)
            
def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        try:
            success, frame = cap.read()  # read the camera frame
            if not success:
                yield (b'--frame\r\n'+
                b'Content-Type: image/jpeg\r\n\r\n' + b'\r\n')  # concat frame one by one and show result
                break
            else:
                ref, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
        except Exception as e:       
            print(f"Something wrong: {e}")       
            yield (b'--frame\r\n'+
                b'Content-Type: image/jpeg\r\n\r\n' + b'\r\n')  # concat frame one by one and show result
            #cap = setCam(0)     
                

@app.route('/video')
def video():        
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():        
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

