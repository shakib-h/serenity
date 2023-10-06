import tkinter as tk
from tkinter import *

stressTest = tk.Tk()
stressTest.title("Stress Test")
stressTest.geometry("500x500")
stressTest.configure(bg="#ffffff")

questions = [
    '''Q1 : How often do you feel overwhelmed with your life?''',
    '''Q2 : Do you struggle to fall asleep at night?''',
    '''Q3 : Do you turn to unhealthy food indulgences such as eating junk food, drinking excessively, or eating sugary foods when feeling overwhelmed?''',
    '''Q4 : Do you experience headaches or muscle tension?''',
    '''Q5 : During work hours, do you have a hard time staying focused and concentrating on the task-at-hand? '''
]
answer_choice = [
    ["Never"],
    ["Sometimes"],
    ["Often"],
    ["Almost_Always"],
]

print("hello")

user_input = []
ques = 0

# Declare question_text and option_buttons as global variables
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
        option_buttons[i].config(text=answer_choice[ques][i])
    #ques_label.config(text=f"Question {ques+1} of {len(questions)}")

def stress_level():
    stress_mapping = {
        '1': 25,
        '2': 50,
        '3': 75,
        '4': 100
    }
    weights = [20, 20, 15, 15, 30]

    stress_result = "Your stress level is: "
    stress_level = 0  

    for i, response in enumerate(user_input):
        stress_level += stress_mapping[str(response + 1)] * (weights[i] / 100)

    stress_result += str(stress_level)
    stress = tk.Label(stressTest, text=stress_result, bg='#ffffff', fg='#111111', font=('Arial', 21))
    stress.pack()

def start():
    label.destroy()
    start_button.destroy()

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    global question_text
    question_text = tk.StringVar()
    question_text.set(questions[ques])

    global option_buttons
    option_buttons = []

    global ques_label

    #for i in range(5):
    question = tk.Label(stressTest, text=questions[0], bg='#ffffff', fg='#111111', font=('Arial', 21))
    question.pack()

    option1 = tk.Radiobutton(stressTest, text=answer_choice[0], bg='#ffffff', fg='#111111', font=('Arial', 16), value=0, variable=radiovar)
    option1.pack()

    option2 = tk.Radiobutton(stressTest, text=answer_choice[1], bg='#ffffff', fg='#111111', font=('Arial', 16), value=1, variable=radiovar)
    option2.pack()

    option3 = tk.Radiobutton(stressTest, text=answer_choice[2], bg='#ffffff', fg='#111111', font=('Arial', 16), value=2, variable=radiovar)
    option3.pack()

    option4 = tk.Radiobutton(stressTest, text=answer_choice[3], bg='#ffffff', fg='#111111', font=('Arial', 16), value=3, variable=radiovar)
    option4.pack()

    option_buttons = [option1, option2, option3, option4]

    next_button = tk.Button(stressTest, text="Next", command=selected, bg='#ffffff', fg='#111111', font=('Arial', 20))
    next_button.pack()

# Widgets
label = tk.Label(stressTest, text="Take a test to check your stress level")
start_button = tk.Button(stressTest, text="Start test", bg='#333333', fg='#ffffff', command=start)
label.pack()
start_button.pack()

stressTest.mainloop()
