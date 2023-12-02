import tkinter as tk
from tkinter import *

class StressTest:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        # self.parent_frame.title("Stress Test")
        # self.parent_frame.geometry("600x600")
        self.parent_frame.configure(bg="#325343")

        self.questions = [
            '''Q1 : How often do you feel overwhelmed with your life?''',
            '''Q2 : Do you struggle to fall asleep at night?''',
            '''Q3 : Do you turn to unhealthy food indulgences such 
                as eating junk food, drinking excessively, or eating 
                sugary foods when feeling overwhelmed?''',
            '''Q4 : Do you experience headaches or muscle tension?''',
            '''Q5 : During work hours, do you have a hard time staying focused and concentrating on the task-at-hand? '''
        ]

        self.answer_choice = [
            ["Never", "Rarely", "Sometimes", "Always"],
            ["Never", "Rarely", "Sometimes", "Always"],
            ["Never", "Rarely", "Sometimes", "Always"],
            ["Never", "Rarely", "Sometimes", "Always"],
            ["Never", "Rarely", "Sometimes", "Always"]
        ]

        self.user_input = []
        self.ques = 0

        self.question_text = None
        self.option_buttons = []

        self.label = tk.Label(self.parent_frame, text="Take a test to check your stress level!", height=2, bg="#325343",
                              font=("Impact", 20), fg="#a6de9b")
        self.start_button = tk.Button(self.parent_frame, height=3, width=10, text="Start test", bg="#325343",
                                      fg='#ffffff', font=("Impact", 20), command=self.start)

        self.label.pack()
        self.start_button.pack()

    def selected(self):
        self.user_input.append(self.radiovar.get())
        self.radiovar.set(-1)

        if self.ques < len(self.questions) - 1:
            self.ques += 1
            self.load_question()
        else:
            self.stress_level()

    def load_question(self):
        self.question_text.set(self.questions[self.ques])
        for i in range(4):
            self.option_buttons[i].config(text=self.answer_choice[self.ques][i], state=NORMAL)

    def stress_level(self):
        stress_mapping = {
            '0': 25,
            '1': 50,
            '2': 75,
            '3': 100
        }
        weights = [20, 20, 15, 15, 30]

        stress_result = "Your stress level is: "
        stress_level = 0

        for i, response in enumerate(self.user_input):
            stress_level += stress_mapping[str(response)] * (weights[i] / 100)

        question_bg = Frame(height=420, width=580, bg="#a6de9b", master=self.parent_frame)
        question_bg.pack()
        stress_result += str(stress_level)
        stress = tk.Label(question_bg, text=stress_result, bg='#325343', fg='#a6de9b', font=('Arial', 21))
        stress.pack()

    def start(self):
        self.label.destroy()
        self.start_button.destroy()
        question_bg = Frame(height=420, width=580, bg="#a6de9b", master=self.parent_frame)
        question_bg.pack()
        self.radiovar = IntVar()
        self.radiovar.set(-1)

        self.question_text = tk.StringVar()
        self.question_text.set(self.questions[self.ques])

        self.option_buttons = []

        ques_label = tk.Label(question_bg, textvariable=self.question_text, bg='#a6de9b', fg='#325343',
                              font=('Arial', 21))
        ques_label.pack()

        for i in range(4):
            option = tk.Radiobutton(question_bg, text="", bg='#a6de9b', fg='#325343', font=('Arial', 16), value=i,
                                    variable=self.radiovar, state=DISABLED)
            option.pack()
            self.option_buttons.append(option)

        self.load_question()

        next_button = tk.Button(question_bg, text="Next", command=self.selected, bg='#325343', fg='#a6de9b',
                                font=('Arial', 20))
        next_button.pack()


    def destroy(self):
        self.parent_frame.destroy()