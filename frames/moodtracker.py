import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class MoodTracker:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.mood_value = 0

        self.feeling_label = ttk.Label(self.parent_frame, text="How are you feeling today?", font=('Arial', 30), anchor='center')
        self.feeling_label.place(x=533, y=150, anchor='center')

        button_font = ('Arial', 36)
        self.happy_button = tk.Button(self.parent_frame, text="😁", command=self.happy_mood, font=button_font)
        self.slightly_happy_button = tk.Button(self.parent_frame, text="🙁", command=self.slightly_happy_mood, font=button_font)
        self.sad_button = tk.Button(self.parent_frame, text="😥", command=self.sad_mood, font=button_font)
        self.crying_button = tk.Button(self.parent_frame, text="😭", command=self.crying_mood, font=button_font)

        mood_label_font = ('Arial', 48)
        self.mood_label = ttk.Label(self.parent_frame, text="Mood:", font=mood_label_font, anchor='center')
        mood_value_label_font = ('Arial', 48)
        self.mood_value_label = ttk.Label(self.parent_frame, text="0%", font=mood_value_label_font, anchor='center')

        self.happy_button.place(x=233, y=300, anchor='center')
        self.slightly_happy_button.place(x=433, y=300, anchor='center')
        self.sad_button.place(x=633, y=300, anchor='center')
        self.crying_button.place(x=833, y=300, anchor='center')
        self.mood_label.place(x=343, y=400, anchor='center')
        self.mood_value_label.place(x=600, y=400, anchor='center')

        self.update_mood_value_label()

    def happy_mood(self):
        self.mood_value = 100
        self.update_mood_value_label()

    def slightly_happy_mood(self):
        self.mood_value = 50
        self.update_mood_value_label()

    def sad_mood(self):
        self.mood_value = 25
        self.update_mood_value_label()

    def crying_mood(self):
        self.mood_value = 5
        self.update_mood_value_label()

    def update_mood_value_label(self):
        self.mood_value_label["text"] = f"{self.mood_value}%"

    def destroy(self):
        self.parent_frame.destroy()