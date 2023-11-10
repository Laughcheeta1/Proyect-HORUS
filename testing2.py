from ultralytics import YOLO
import cv2
import sys

videoInput = cv2.VideoCapture("C:\\Users\\Usuario\\Documents\\Universidad\\Requisitos y modelos\\CODE\\videosTest\\Lockheed Martin  F-35 Lightning II.mp4") # Give the video in question
model = YOLO("C:\\Users\\Usuario\\Documents\\Universidad\\Requisitos y modelos\\CODE\\previousTraining.pt")

if not videoInput.isOpened():
    print(f"Problems accesing the file")
    sys.exit()

while videoInput.isOpened():
    success, frame = videoInput.read()

    if not success:
        print("There was an issue reading the frame")
        continue
    
    # TODO: understand better from here to the bottom
    results = model(frame, show = True)