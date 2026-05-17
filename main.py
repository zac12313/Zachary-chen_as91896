


import os
import tkinter
from tkinter import *
#2nd window
root=Tk()
def open_new_window1():
    new_window=tkinter.Toplevel(root)
    new_window.geometry("1280x720")
    new_window.img_ref = PhotoImage(file="Photo/Q1.png")
    bg_label = Label(new_window, image=new_window.img_ref)
    bg_label.pack(fill="both", expand=True)

def switch_window1():
    root.destroy()








#size of window
root.geometry("1141x639")
#background
bg = PhotoImage(file="Photo/Homepage.png")

canvas1 = Canvas(root, width=1141, height=639)
canvas1.pack(fill="both",expand=True)

canvas1.create_image(0,0, image=bg, anchor="nw")
#Creating buttons
button1 = Button(root, text="start", command=open_new_window1,)
button2 = Button(root,text="Name")

button1_canvas = canvas1.create_window(
    100,
    10,
    anchor="nw",
    window=button1,
)
button2_canvas = canvas1.create_window(
    100,
    10,
    anchor="nw",
    window=button2,
)
button1.place(x=599, y=453)
button2.place(x=265, y=453)


button1.config(width=39, height=5)
button2.config(width=39, height=5)



root.title("Gym quiz")








root.mainloop()