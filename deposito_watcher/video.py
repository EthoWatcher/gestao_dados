
import cv2

def abre_video(name_path):
    cap = cv2.VideoCapture(name_path)
    i = 0
    while(1):
        i +=1
        _, frame = cap.read()
        cv2.imshow("frame", frame)
        k = cv2.waitKey(1)
        if k == 27:
            break
        if i == 100:
            break

    cap.release()
    cv2.destroyAllWindows()
    return 0