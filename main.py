import tkinter as tk

from tkinter import *


from PIL import Image, ImageTk

import random




class Quizstart:
    def __innit__(self, parent):
        background_color= "#F4F4EF"
        self.quiz_frame = Frame(parent, bg=background_color,padx=67, pady=67)
        self.quiz_frame.grid()

        self.heading_label = Label(self.quiz_frame, text="Gym quiz",bg=background_color)
        self.heading_label.grid(row=0,padx=20, pady=10)






root=Tk()































































root.mainloop()