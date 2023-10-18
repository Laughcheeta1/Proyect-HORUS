from ultralytics import YOLO

if __name__ == '__main__':
    # Load Model
    model = YOLO("yolov8n.yaml") # build a new model from scratch

    # Use the model
    results = model.train(data="config.yaml", epochs = 100) # train the model