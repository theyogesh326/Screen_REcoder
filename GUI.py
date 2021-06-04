'''import tkinter
import tkinter as tk  # Starting code
from tkinter import ttk
win = tk.Tk()
win.geometry('200x150')
win.title('Screen Recoder')
def start():
    start()
b1 = tk.Button(win,text ="start",width = 12,bg ='red',fg = 'green')
b1.place(x=180,y=180)
def Stop():
    Stop()
b2 = tk.Button(win,text="Stop",width=12,bg='Blue',fg = 'red')
b2.place(x=180,y=180)
win.mainloop()
'''

import tkinter
#import tkinter as tk
from tkinter import *

root = Tk ()
root.geometry('100x100')

btn = Button(root,text = ' click here to start screen Recoder', bd = '5',)

btn.pack(side ='top' )

btn = Button(root,text = 'stop the recorder', bd = '5',)
btn.pack(side ='top' )

root.mainloop()


