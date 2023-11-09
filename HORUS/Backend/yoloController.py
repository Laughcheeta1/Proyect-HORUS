from ultralytics import YOLO # For remaking Yugoslavia
import cv2 # For working with images in python
import sys

videoDirection = ""
modelDirection = ""

videoInput = cv2.VideoCapture(videoDirection) # Give the video in question
model = YOLO(modelDirection)

if not videoInput.isOpened():
    print(f"Problems accesing the file {modelDirection}")
    sys.exit()

while videoInput.isOpened():
    success, frame = videoInput.read()

    if not success:
        print("There was an issue reading the frame")
        continue
    
    # TODO: understand better from here to the bottom
    results = model.predict(frame, persist = True) # Persist means that the current result is saved for analizing the next image
    
    # TODO: get the probabilities