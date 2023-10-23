import tkinter as tk
from tkinter import *

stressTest = tk.Tk()
stressTest.title("Stress Test")
stressTest.geometry("600x600")
stressTest.configure(bg="#325343")

questions = [
    '''Q1 : How often do you feel overwhelmed with your life?''',
    '''Q2 : Do you struggle to fall asleep at night?''',
    '''Q3 : Do you turn to unhealthy food indulgences such 
        as eating junk food, drinking excessively, or eating 
        sugary foods when feeling overwhelmed?''',
    '''Q4 : Do you experience headaches or muscle tension?''',
    '''Q5 : During work hours, do you have a hard time staying focused and concentrating on the task-at-hand? '''
]

answer_choice = [
    ["Never", "Rarely", "Sometimes", "Always"],
    ["Never", "Rarely", "Sometimes", "Always"],
    ["Never", "Rarely", "Sometimes", "Always"],
    ["Never", "Rarely", "Sometimes", "Always"],
    ["Never", "Rarely", "Sometimes", "Always"]
]

user_input = []
ques = 0

question_text = None
option_buttons = []

def selected():
    global ques
    user_input.append(radiovar.get())
    radiovar.set(-1)  # Reset the radio button selection

    if ques < len(questions) - 1:  # Check if there are more questions
        ques += 1
        load_question()
    else:
        stress_level()


def load_question():
    global ques
    question_text.set(questions[ques])
    for i in range(4):
        option_buttons[i].config(text=answer_choice[ques][i], state=NORMAL) # [MODIFIED] 'state=NORMAL' added [cause of non-error code now]

def stress_level(): # [MODIFIED] numbers got modified
    stress_mapping = {
        '0': 25,
        '1': 50,
        '2': 75,
        '3': 100
    }
    weights = [20, 20, 15, 15, 30]

    stress_result = "Your stress level is: "
    stress_level = 0  

    for i, response in enumerate(user_input):
        stress_level += stress_mapping[str(response)] * (weights[i] / 100)
    question_bg = Frame(height=420, width=580, bg="#a6de9b")
    question_bg.pack()
    stress_result += str(stress_level)
    stress = tk.Label(question_bg, text=stress_result, bg='#325343', fg='#a6de9b', font=('Arial', 21))
    stress.pack()



def start():
    label.destroy()
    start_button.destroy()
    question_bg = Frame(height=420, width=580, bg="#a6de9b")
    question_bg.pack()
    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    global question_text
    question_text = tk.StringVar()
    question_text.set(questions[ques])

    global option_buttons
    option_buttons = []

    global ques_label
  
    ques_label = tk.Label(question_bg, textvariable=question_text, bg='#a6de9b', fg='#325343', font=('Arial', 21))
    ques_label.pack()
    
    # [MODIFIED] updated whole platform
    for i in range(4):
        option = tk.Radiobutton(question_bg, text="",  bg='#a6de9b', fg='#325343', font=('Arial', 16), value=i, variable=radiovar, state=DISABLED)
        option.pack()
        option_buttons.append(option)

    load_question()  # [MODIFIED] Added this line to load the first question

    next_button = tk.Button(question_bg, text="Next", command=selected, bg='#325343', fg='#a6de9b', font=('Arial', 20))
    next_button.pack()


# Widgets
label = tk.Label(stressTest, text="Take a test to check your stress level!",height=2, bg="#325343",font=("Impact", 20), fg="#a6de9b")
start_button = tk.Button(stressTest,height=3,width=10, text="Start test", bg="#325343", fg='#ffffff',font=("Impact", 20), command=start)
label.pack()


start_button.pack()

stressTest.mainloop()
