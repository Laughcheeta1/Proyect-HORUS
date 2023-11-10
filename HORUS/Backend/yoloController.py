from ultralytics import YOLO # For remaking Yugoslavia
import cv2 # For working with images in python

class model:
    _modelDirection = ""

    def __init__(self, videoDirection):
        # self.videoDirection = videoDirection
        self.videoInput = cv2.VideoCapture(videoDirection)
        self.model = YOLO(self._modelDirection)

        if not self.videoInput.isOpened(): # Check if the video can be opened
            return None
        
    def readFrame(self):
        if self.videoInput.isOpened(): # Check if the video is still opened
            success, frame = self.videoInput.read() # Read the frame

            if success: # Check if the frame has been read

                # From the model result ([0] because it is a list, but a list of only 1 element jajaja), get the boxes, convert it to 
                # cpu, then convert it to numpy, and after that, get the classes that have been detected
                return model.predict(frame, show = True, persist = True)[0].boxes.cpu().numpy().cls
                    # TODO: Decide whether to return only the clases, or also the bounding boxes
        
        return None # If either the video is not opened or the frame could be read, then return null
        

    # def startDetection(self):
        # videoInput = cv2.VideoCapture(self.videoDirection) # Give the video in question
        # model = YOLO(self._modelDirection)

        # if not videoInput.isOpened():
        #     print(f"Problems accesing the file {self.videoDirection}")
        #     sys.exit()

        # while videoInput.isOpened():
        #     success, frame = videoInput.read()

        #     if not success:
        #         print("There was an issue reading the frame")
        #         continue
            
        #     # TODO: understand better from here to the bottom
        #     results = model.predict(frame, show = True, persist = True) # Persist means that the current result is saved for analizing the next image
            
        #     # TODO: get the probabilities