import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import cvzone
import numpy as np
from pynput.keyboard import Controller

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)
keyboard = Controller()

# def draw_all(img, button_list):
#     for button in button_list:
#         x, y = button.pos
#         w, h = button.size
#         cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 233), cv2.FILLED)
#         cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
#     return img


def draw_all(img, buttonList):
    imgNew = np.zeros_like(img, np.uint8)
    for button in buttonList:
        x, y = button.pos
        cvzone.cornerRect(imgNew, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
                          20, rt=0)
        cv2.rectangle(imgNew, button.pos, (x + button.size[0], y + button.size[1]),
                      (1, 1, 1), cv2.FILLED)
        cv2.putText(imgNew, button.text, (x + 40, y + 60),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)

    out = img.copy()
    alpha = 0.5
    mask = imgNew.astype(bool)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
    return out


class Button:
    def __init__(self,pos, text, size=[85,85]):
        self.pos = pos
        self.size = size
        self.text = text


button_list = []
final_text = []
keys = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '.']]
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        button_list.append(Button([100 * j + 100, 100 * i + 50], key))


while True:
    success, frame = cap.read()
    img = cv2.flip(frame, 1)
    img = detector.findHands(img)
    landmark_list, bounding_box = detector.findPosition(img)
    img = draw_all(img, button_list)

    if landmark_list:
        for button in button_list:
            x, y = button.pos
            w, h = button.size

            if x < landmark_list[8][0] < x + w and y < landmark_list[8][1] < y + h:
                cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                length, _, _ = detector.findDistance(8,12,img)

                if length < 40:
                    keyboard.press(button.text)
                    cv2.rectangle(img, button.pos, (x + w, y + h), (0, 250, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                    final_text += button.text
                    sleep(0.5)

    cv2.rectangle(img, (50, 350), (700, 450), (255, 255, 255), cv2.FILLED)
    cv2.putText(img, ''.join(final_text), (60, 425), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)

    cv2.imshow('Image', img)
    cv2.waitKey(1)
