import tkinter as tk

from tkinter import *


from PIL import Image, ImageTk


import random

#QUestion dictionary
questions_and_answers ={
    1: ["What piece of equipment can be used  to train the pectoral muscles?",'Treadmill','Bench press','Rowing Machine','Kettlebell', 3],
2: ["What are the chest Muscles called",'Abdominal','Biceps','Pectorals','Deltoids', 3],
3: ["What is the largest muscle group in the body",'Pectorals','Biceps','Gluteus Maximus','Abdominal', 3],
4: ["How many calories are in 1 gram of Carbohydrates",'1','3','7','4', 4],
5: ["How much protein do you need per kg of budy weight for muscle gain ",'1-1.5','0.3x-1','1.6-2.2','3-5', 1],
6: ["How many reps to failure should you do for maximum hypertrophy",'0-4','6-8','10-12','14+', 2],
7: ["How many seconds should the eccentric be for better hypertrophy",'0-1.5','2-4','5-7','8+', 2],
8: ["What are some things you should do before your workout",'Drink 500-600ml of water 2hours before','Eat 30 grams of carbs 0-30 minutes before','Stretch','All of the above', 4],
9: ["How many sets per week per muscle group",'0-8','10-20','21-25','26-30', 2],
10: ["How much grams of protein should you eat post-workout",'0-15','20-40','0-5','6-14', 2],
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

    def name_collection(self):
        name = self.entry_box.get()
        if name:
            names.append(name)
            self.quiz_frame.destroy()
            Quiz(root)


class Quiz:
    def __init__(self, parent):
        background_color = "oldLace"
        self.quiz_frame = Frame(parent, bg=background_color, padx=200, pady=100)
        self.quiz_frame.grid()

        randomiser()

        self.question_label = label(self.quiz_frame, text=questions_and_answers[qnum][0], font=("Tw Cen MT", "18", "bold"), bg=background_color)
        self.question_label.grid(row=0, padx=10, pady=10)

        self.var1 = IntVar()

        self.rb1 = Radiobutton(self.quiz_frame, text=questions_and_answers[qnum][1], font=("Helvetica","12"), bg=background_color, value=1, variable=self.var1)
        self.rb1.grid(row=1, sticky=W)









root=Tk()































































root.mainloop()