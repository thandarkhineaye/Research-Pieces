import threading
import winsound
import cv2
import imutils

# initialization for camera
# parameter 0~n is the number of cameras
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
print(cam)
# set the frame rate
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 648)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 648)

_, start_frame = cam.read()
start_frame = imutils.resize(start_frame, width=500)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (21,21), 0)

alarm = False
alarm_mode = False
alarm_counter = 0

# function to call when alarm happened
def beep_alarm():
    global alarm
    for _ in range(5):
        if not alarm_mode:
            break
        print("ALARM")
        winsound.Beep(2500,1000)
    alarm= False

while True:
    _, frame = cam.read()
    frame = imutils.resize(frame, width=500)

    # Movement tracking by compare frames
    if alarm_mode:
        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_bw = cv2.GaussianBlur(frame_bw,(5,5), 0)

        difference = cv2.absdiff(frame_bw, start_frame)
        threshold = cv2.threshold(difference,25,255,cv2.THRESH_BINARY)[1]
        start_frame = frame_bw

        # can arrange number to detect movement rates
        if threshold.sum() > 300:
            alarm_counter += 1
        else:
            if alarm_counter > 0:
                alarm_counter -= 1
        cv2.imshow("Cam", threshold)
    else: 
        cv2.imshow("Cam", frame)

    if alarm_counter > 20:
        if not alarm:
            alarm = True
            threading.Thread(target = beep_alarm).start()

    # initialize key_pressed
    key_pressed = cv2.waitKey(38)

    if key_pressed == ord("t"):
        alarm_mode = not alarm_mode
        alarm_counter = 0;
    # setting key_pressed
    if key_pressed == ord("q"):
        alarm_mode = False
        break

cam.release()
cv2.destroyAllWindows()
