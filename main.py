


import os
from tkinter import *

root=Tk()
#size of window
root.geometry("1141x639")
#background
bg = PhotoImage(file="Photo/Homepage.png")

canvas1 = Canvas(root, width=1141, height=639)
canvas1.pack(fill="both",expand=True)

canvas1.create_image(0,0, image=bg, anchor="nw")

button1 = Button(root, text="start", borderwidth=0,highlightthickness=0)
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
button1.place(x=700, y=10)
root.title("Gym quiz")






root.mainloop()