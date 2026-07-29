
from tkinter import *


from PIL import Image, ImageTk


import random






#Question dictionary
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

names = []
asked = []
score = 0
qnum = 0

def randomiser():
    global qnum

    while True:
        qnum = random.randint(1, 10)

        if qnum not in asked:
            asked.append(qnum)
            break









class Quizstart:
    def __init__(self, parent):
        background_color = "#F4F4EF"
        self.quiz_frame = Frame(parent, bg=background_color, padx=67, pady=67)
        self.quiz_frame.grid()

        self.heading_label = Label(self.quiz_frame, text="Gym quiz", bg=background_color)

        self.heading_label.grid(row=0, padx=20, pady=10)

        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=2, padx=20, pady=20)

        self.continue_button = Button(self.quiz_frame, text="continue", bg="grey", command=self.name_collection)
        self.continue_button.grid(row=6, padx=20, pady=20)

        try:
            self.photo = Image.open("photo.png")
            self.photo = self.photo.resize((200, 150))
            self.photo = ImageTk.PhotoImage(self.photo)
            self.image_label = Label(
              self.quiz_frame,
              image=self.photo,
              bg=background_color
            )

            self.image_label.grid(row=4,  padx=10, pady=10)
        except:
            print("image not found")



    def name_collection(self):

        name = self.entry_box.get()
        if name:
            names.append(name)
            self.quiz_frame.destroy()
            Quiz(root)


class Quiz:
    def __init__(self, parent):

        global score
        background_color = "oldLace"
        self.quiz_frame = Frame(
            parent, bg=background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        randomiser()

        self.question_label = Label(self.quiz_frame, text=questions_and_answers[qnum][0],  bg=background_color)
        self.question_label.grid(row=0, padx=10, pady=10)

        self.var1 = IntVar()

        self.rb1 = Radiobutton(
            self.quiz_frame,
            text=questions_and_answers[qnum][1],
            value=1,
            variable=self.var1,
            bg=background_color
        )
        self.rb1.grid(row=1, sticky=W)

        self.rb2 = Radiobutton(
            self.quiz_frame,
            text=questions_and_answers[qnum][2],
            value=2,
            variable=self.var1,
            bg=background_color
        )
        self.rb2.grid(row=2, sticky=W)

        self.rb3 = Radiobutton(
            self.quiz_frame,
            text=questions_and_answers[qnum][3],
            value=3,
        variable = self.var1,
        bg = background_color
        )
        self.rb3.grid(row=3, sticky=W)

        self.rb4 = Radiobutton(
            self.quiz_frame,
            text=questions_and_answers[qnum][4],
            value=4,
        variable = self.var1,
        bg = background_color
        )
        self.rb4.grid(row=4, sticky=W)

        self.score_label = Label(
            self.quiz_frame,
            text=f"score: {score}",
            bg=background_color
        )

        self.score_label.grid(row=6)
        self.confirm_button = Button(self.quiz_frame, text="confirm", bg="pink", command=self.test_progress)
        self.confirm_button.grid(row=8,pady=10)

    def questions_setup(self):
            randomiser()
            self.var1.set(0)
            self.question_label.config(text=questions_and_answers[qnum][0])
            self.rb1.config(text=questions_and_answers[qnum][1])
            self.rb2.config(text=questions_and_answers[qnum][2])
            self.rb3.config(text=questions_and_answers[qnum][3])
            self.rb4.config(text=questions_and_answers[qnum][4])

    def test_progress(self):
            global score
            choice = self.var1.get()
            if choice == 0:
                self.confirm_button.config(text="Please select answer")
                return

            #check answer
            if choice == questions_and_answers[qnum][5]:
                score += 1
                self.score_label.config(text=f"Score: {score}")
            else:
                correct = questions_and_answers[qnum][5]
                self.score_label.config(text=f"Wrong correct:{questions_and_answers[qnum][correct]}")

            if len(asked) >= 5:
                self.quiz_frame.destroy()
                self.display_summary()
            else:
                self.questions_setup()


    def display_summary(self):
            summary_frame = Frame(root,bg="Oldlace", padx=100, pady=100)
            summary_frame.grid()

            final_msg = f"Quiz Completed!\nYour final score is {score} out of 5"
            summary_label =Label(summary_frame, text=final_msg, font=("Tw Cen MT", 18, "bold"), bg="OldLace")
            summary_label.grid(row=0, pady=20)

            exit_button = Button(summary_frame, text="Exit", command=root.destroy, bg="red", fg="white")
            exit_button.grid(row=1, pady=10)

    if __name__ == "__main__":
        root = Tk()
        root.title("Quiz")

        img = Image.open("2.png")
        img = img.resize((200,150))
        photo = ImageTk.PhotoImage(img)

        quiz_instance = Quizstart(root)
        root.mainloop()



