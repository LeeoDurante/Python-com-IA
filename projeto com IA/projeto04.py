import cv2 
from cvzone.HandTrackingModule import HandDetector


webcam = cv2.VideoCapture(0)
traker = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    sucess, image = webcam.read()
    coordinates, HandsImage = traker.findHands(image)

    print(coordinates)


    cv2.imshow("Projeto04 - IA", image)

    if cv2.waitKey(1) != -1:
        break

webcam.release()
cv2.destroyAllWindows()