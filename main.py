import datetime
from PIL import ImageGrab
import  numpy as np
import  cv2
import tkinter
from tkinter import  *
root = Tk()
btn = Button(root,text = ' click here to start screen Recoder', bd = '5',)

btn.pack(side ='top' )

btn = Button(root, text='stop the recorder', bd='5', )
btn.pack(side='top')
root.mainloop()


from  win32api import GetSystemMetrics
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
file_name =f'{time_stamp}.mkv'
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
capture_video = cv2.VideoWriter(file_name, fourcc ,20.0,(width,height))
webcam = cv2.VideoCapture(0)
print(width,height)
while True:
    img = ImageGrab.grab(bbox=(0, 0, width,height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    _,frame = webcam.read()
    fr_height,fr_width, _ = frame.shape
    img_final[0:fr_height,0:fr_width, :] =frame[0 : fr_height,0:fr_width, : ]
    cv2.imshow('Secret capture',img_final)
    cv2.imshow('webcam',frame)
    capture_video.write(img_final)
    if cv2.waitKey(10) ==ord('q'):
         break



