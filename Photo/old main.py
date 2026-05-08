import tkinter as tk
from tkinter import *

root= tk.Tk()
#size of window
root.geometry("1280x720")
#background
bg = PhotoImage(file="Photo/Homepage.png")

canvas1=Canvas(root, width=1280, height=720)
canvas1.pack(fill="both",expand=True)

canvas1.create_image(0,0, image=bg, anchor="nw")


label=tk.Label(root, text="bomboclatt quiz",bg="yellow")


tk.Label(root, text="First Name",bg="pink")
tk.Label(root, text="Last Name",bg="pink")
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)



root.title("Gym quiz")

button = tk.Button(root,text="Exit", width=12,command=root.destroy)





root.mainloop()