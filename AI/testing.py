from ultralytics import YOLO

model = YOLO("C:\\Users\\Usuario\\Documents\\Universidad\\Requisitos y modelos\\CODE\\runs\\detect\\train20\weights\\best.pt")

model.predict("C:\\Users\\Usuario\\Downloads\\TestAI.mp4", save = True, show = True, conf = 0.7)