import tkinter as tk

from tkinter import *


from PIL import Image, ImageTk

import random


questions_andanswers ={
    1: ("What piece of equipment can be used  to train the pectoral muscles?",'Treadmill','Bench press','Rowing Machine','Kettlebell', 3),
2: ("What are the chest Muscles called",'Abdominals','Biceps','Pectorals','Deltoids', 3),
3: ("What is the largest muscle group in the body",'Pectorals','Biceps','Gluteus Maximus','Abdominals', 3),
4: ("How many calories are in 1 gram of Carbohydrates",'1','3','7','4', 4),
5: ("How much protein do you need per kg of budy weight for muscle gain ",'1-1.5','0.3x-1','1.6-2.2','3-5', 1),
1: ("",'','','','', 1),
1: ("",'','','','', 1),
1: ("",'','','','', 1),
1: ("",'','','','', 1),
1: ("",'','','','', 1),
1: ("",'','','','', 1),


















}

class Quizstart:
    def __innit__(self, parent):
        background_color= "#F4F4EF"
        self.quiz_frame = Frame(parent, bg=background_color,padx=67, pady=67)
        self.quiz_frame.grid()

        self.heading_label = Label(self.quiz_frame, text="Gym quiz",bg=background_color)
        self.heading_label.grid(row=0,padx=20, pady=10)

        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=2, padx=20, pady=20)

        self.continue_button = Button(self.quiz_frame, text="continue",bg="grey", command=self.name_collection)
        self.continue_button.grid(row=6, padx=20, pady=20)

        self.image_label = Label(self.quiz_frame,image="../Photo/Homepage.png")
        self.image_label.image = photo
        self.image_label.grid(row=4, padx=10,pady=10)






root=Tk()































































root.mainloop()