import tkinter
from Service import Service
import tkinter.messagebox
from tkinter import filedialog
import customtkinter
from PIL import Image, ImageTk
import cv2

class ImageApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Yugoslavia bro")
        self.geometry(f"{1100}x{580}")
        self.label = tkinter.Label(self, image=None)

    
    def changeImage(self, im):
        b, g, r = cv2.split(im)
        im = cv2.merge((r,g,b))
        img = Image.fromarray(im)
        imgtk = ImageTk.PhotoImage(image = img)
        tkinter.Label(self, image = imgtk).pack()
        print("Image has been changed")
