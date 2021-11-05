from cv2 import VideoCapture, cvtColor, imshow, CAP_DSHOW, COLOR_BGR2GRAY, waitKey, destroyAllWindows
from time import sleep

video = VideoCapture(0, CAP_DSHOW)

# how many frames are generated
a = 1

while True:
    a += 1

    # activate camera
    check, frame = video.read()

    # print(check)
    print(frame)

    gray = cvtColor(frame, COLOR_BGR2GRAY)
    # sleep(3)
    imshow("Capturing", gray)

    key = waitKey(1)

    if key == ord('q'):
        break

print("Frames captured:", a)
video.release()
destroyAllWindows()