from ultralytics import YOLO

if __name__ == '__main__':
    # Load Model
    model = YOLO("C:\\Users\\Asus\\Desktop\\ProyectoHorus\\modeloAnterior.pt") # build a new model from scratch

    # Use the model
    results = model.train(data="AI\config.yaml", epochs =100) # train the model