from ultralytics import YOLO

model = YOLO("C:\\Users\\Asus\\Desktop\\ProyectoHorus\\runs\\detect\\train8\\weights\\best.pt")

model.predict("C:\\Users\\Asus\\Desktop\\ProyectoHorus\\videosTest\\y2mate.com - 10 Minutes of FIGHTER JETS in Action_480p.mp4", save = True, show = True, conf = 0.7)