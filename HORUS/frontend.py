import os
import sys

import tkinter
import Service
import tkinter.messagebox
from tkinter import filedialog
import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("HORUS AI Object Detector")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
       
        self.grid_rowconfigure((0, 1), weight=1)

        def pathFile():
           filePath = filedialog.askopenfilename()
           self.entry_path.delete(0,tkinter.END)
           self.entry_path.insert(0,filePath)

        def startRecording():
            videoPath = self.entry_path.get()
            serv = Service(videoPath)

            while True:
                listOfPlanes, numberOfPlanes = serv.readFrame()

                if not serv.successful:
                    break

                for plane in listOfPlanes:
                    
                    name = plane["name"]
                    purpose = plane["purpose"]
                    armament = plane["armament"]
                    maxSpeed = plane["max_speed"]
                    maxRange = plane["max_range"]
                    quantityOfThePlane = numberOfPlanes[plane["classNumber"]]
                    direccionImagen = f"./AIRPLANES/{plane['className']}.jpg"

                    label_image= customtkinter.CTkLabel(self.intFrame, image= customtkinter.CTkImage(dark_image=Image.open(f"./AIRPLANES/{plane['className']}.jpg"), size=(400,300)), text=" ")
                    label_image.pack(side = "top")
                    label_dentro1 = customtkinter.CTkLabel(self.intFrame, font=customtkinter.CTkFont(size=11, weight="bold"), text=f"- Name: {name}")
                    label_dentro1.pack(side = "top")
                    label_dentro2 = customtkinter.CTkLabel(self.intFrame, font=customtkinter.CTkFont(size=11, weight="bold"), text=f"- Purpose: {purpose}")
                    label_dentro2.pack(side = "top")
                    label_dentro3 = customtkinter.CTkLabel(self.intFrame, font=customtkinter.CTkFont(size=11, weight="bold"), text=f"- Armament: {armament}")
                    label_dentro3.pack(side = "top")
                    label_dentro4 = customtkinter.CTkLabel(self.intFrame, font=customtkinter.CTkFont(size=11, weight="bold"), text=f"- Max Speed: {maxSpeed}")
                    label_dentro4.pack(side = "top")
                    label_dentro5 = customtkinter.CTkLabel(self.intFrame, font=customtkinter.CTkFont(size=11, weight="bold"), text=f"- Max Range: {maxRange}")
                    label_dentro5.pack(side = "top")
                    label_dentro6 = customtkinter.CTkLabel(self.intFrame, font=customtkinter.CTkFont(size=11, weight="bold"), text=f"- Quantity: {quantityOfThePlane}")
                    label_dentro6.pack(side = "top")

                # Show the planes

                

            # Clear the planes from interface

            # List of planes = 
            # [{
            #     '_id': ObjectId('65492f38a58418bb8f2611f9'), 
            #     'className': 'F16', 
            #     'name': 'F16 Fighting Falcon', 
            #     'purpose': 'Interceptacion de aviones enemigos y ataque a tierra', 
            #     'armament': 'Cañon M61 Vulcan y bombas convencionales guiadas por lasers y GPS', 
            #     'max_speed': '2414 Km/h', 
            #     'max_range': '2400 Km', 
            #     'classNumber': 16
            # },
            # {
            #        
            # }
            # ]

            # (the first number (key) is the class of the object, the second (value) is the number of times it appears)
            # Number of planes = 
            # {
            #     16: 1
            # }


        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="HORUS AI", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.entry_path = customtkinter.CTkEntry(self.sidebar_frame,placeholder_text="Archive path")
        self.entry_path.grid(row=2,column=0, padx = 20, pady = 5)
        self.label_path = customtkinter.CTkLabel(self.sidebar_frame,text="Enter the location of the video", font=customtkinter.CTkFont(size=12) )
        self.label_path.grid(row=1,column = 0, padx = 20, pady = 0)
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,  command = pathFile, text="Select Path")
        self.sidebar_button_1.grid(row=3, column=0, padx=20, pady=0)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=startRecording, text="Start recording",fg_color="green")
        self.sidebar_button_2.grid(row=4, column=0, padx=20, pady=10)
      
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        


      

       

        self.intFrame = customtkinter.CTkScrollableFrame(master = self, width= 600, height=500)
        self.intFrame.grid( row = 0, column = 1, padx = 5, pady = 5, ipadx = 5, ipady = 5, rowspan = 2, columnspan = 2)

    



        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=2, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=9, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

        # set default values

        self.appearance_mode_optionemenu.set("Dark")
   
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()
        


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")
