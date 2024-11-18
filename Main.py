import ctypes
import time
from PIL import Image

gif_path = input("Enter File Path: (e.g: C:/Users/Amir/Downloads/Test.gif): ")
temp_path = input("Enter Temp Path: (e.g: C:/Users/Amir/Desktop/Temp.bmp): ") #temp file to store gif frames

def setBackground(path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)

def processFrames(file_path):
    with Image.open(file_path) as gif:
        try:
            while True:
                gif.save(temp_path, format="BMP")

                setBackground(temp_path)

                frame_duration = gif.info.get("duration", 100) / 1000.0 #Get the duration in seconds 
                time.sleep(frame_duration)

                #Move to next frame:
                gif.seek(gif.tell() + 1) #"This frame + 1"

        except EOFError:
            # End of frames
            print("No other frame detected, restarting")
            processFrames(gif_path)

processFrames(gif_path)
