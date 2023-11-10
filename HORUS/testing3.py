from Service import Service

serv = Service("C:\\Users\\Usuario\\Documents\\Universidad\\Requisitos y modelos\\CODE\\videosTest\\20 MINUTES of SUPER CLOSE UP TAKEOFFS & LANDINGS at LHR  4K  London Heathrow Plane Spotting (2023).mp4")

while True:
    lis, dic = serv.readFrame()

    if not serv.successful:
        break
    
    print(lis)
    print(dic)
    