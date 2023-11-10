import ultralytics

model = ultralytics.YOLO("C:\\Users\\Usuario\\Documents\\Universidad\\Requisitos y modelos\\CODE\\previousTraining.pt")
results = model("C:\\Users\\Usuario\\Documents\\Universidad\\Requisitos y modelos\CODE\\videosTest\\planes.png", show = True)

print(results[0].boxes.cpu().numpy().cls)