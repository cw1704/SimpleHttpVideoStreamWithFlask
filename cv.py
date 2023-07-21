import cv2

capture = cv2.VideoCapture(0)
frame = capture.read()

while(True):
    try:
        success, frame = capture.read()
        
        if not success:
            print("can not read")
            break
            
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        
        if cv2.waitKey(1) == ord('q'):
            break

    except Exception as e:
        print(e)
