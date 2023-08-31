# Source: https://stackoverflow.com/questions/72120491/python-opencv-multiprocessing-cv2-videocapture-mp4
import multiprocessing as mp
import cv2, time

def capture_frames():
    src = 0#'test.mp4'
    capture = cv2.VideoCapture(src)
    capture.set(cv2.CAP_PROP_BUFFERSIZE, 2)

    # FPS = 1/X, X = desired FPS
    FPS = 1/120
    FPS_MS = int(FPS * 1000)

    while True:
        # Ensure camera is connected
        if capture.isOpened():
            (status, frame) = capture.read()
            
            # Ensure valid frame
            if status:
                cv2.imshow('frame', frame)
            else:
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            time.sleep(FPS)

    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    print('Starting video stream')
    capture_process = mp.Process(target=capture_frames, args=())
    capture_process.start()
