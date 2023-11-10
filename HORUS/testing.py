from ultralytics import YOLO

model = YOLO("C:\\Users\\Usuario\\Documents\\Universidad\\Requisitos y modelos\\CODE\\trainingThatWorks.pt")
videoLocation = "C:\\Users\\Usuario\\Documents\\Universidad\\Requisitos y modelos\\CODE\\videosTest\\Lockheed Martin  F-35 Lightning II.mp4"

model(videoLocation, show = True)