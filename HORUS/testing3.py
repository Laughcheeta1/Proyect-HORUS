from Backend.Service import Service

serv = Service("C:\\Users\\Usuario\\Documents\\Universidad\\Requisitos y modelos\\CODE\\videosTest\\Lockheed Martin  F-35 Lightning II.mp4")

while True:
    lis, dic = serv.readFrame()

    if not serv.successful:
        break
    
    print(lis)
    print(dic)
    