import tkinter as tk
from tkinter import font, PhotoImage

root= tk.Tk()
#size of window
root.geometry("1280x720")
#background
bg = PhotoImage(file="Photo/Homepage.png")

canvas1= canvas(root, width=1280, height=720)
canvas1.pack(fill="both",expand=True)

canvas1.create_image(0,0, image=bg, anchor="nw")
my_font = font.Font(family="open sans", size=16, weight="bold")

label=tk.Label(root, text="bomboclatt quiz",bg="yellow",font=my_font).grid(row=0, column=1)


tk.Label(root, text="First Name",bg="pink").grid(row=6, column=0)
tk.Label(root, text="Last Name",bg="pink").grid(row=7, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=6, column=1)
entry2.grid(row=7, column=1)

root.title("Gym quiz")

button = tk.Button(root,text="Exit", width=12,command=root.destroy).grid(row=0)





root.mainloop()