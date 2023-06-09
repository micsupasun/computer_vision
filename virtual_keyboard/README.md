# README
## Introduction
This code is a short script that performs a specific function or task. Please specify the details of the code, including what it does, how it works, and any necessary setup or dependencies required to run the code.

## Requirements
List any necessary dependencies, tools, or packages required to run the code. Be specific and include version numbers, if applicable.

## Usage
Provide step-by-step instructions on how to run the code, including any necessary command line arguments, environment variables, or configuration files.

# Explanation
The code is a computer vision project to detect hand gestures and translate them into keyboard inputs.

The first part of the code captures video frames using the cv2.VideoCapture() method and sets the width and height of the frames. Then, the HandDetector class from the cvzone.HandTrackingModule library is initialized to detect hands in the video frames. The keyboard inputs are captured using the pynput.keyboard.Controller class.

The draw_all function takes an image and a list of buttons as inputs, draws the buttons on the image and returns the modified image. Each button has a position, size, and text. The class "Button" is used to initialize the buttons, and a list of buttons is created with the keys of a keyboard.

The main loop continuously captures video frames and finds hands in the frames using the findHands() method of the HandDetector class. The landmark points and the bounding box of the hand are obtained using the findPosition() method. The buttons are drawn on the frame using the draw_all function. If a hand is detected and the hand's landmark point number 8 (little finger) is inside a button's bounding box, the length between the little finger and the thumb is calculated using the findDistance() method. If the length is less than 40, the corresponding keyboard key is pressed, and the button's text is added to the final_text list. The final text is displayed on the frame as a string.
![VirtualKeyboard](https://github.com/micsupasun/computer_vision/blob/main/virtual_keyboard/image_vr.png)



