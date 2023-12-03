from datetime import datetime
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import helper

class Exercise:
    def __init__(self, parent_frame, displayname):
        self.parent_frame = parent_frame
        self.displayname = displayname
        # self.happy_button = tk.Button(self.parent_frame, text="😁", font=('Roboto', 36))
        # self.slightly_happy_button = tk.Button(self.parent_frame, text="🙁", font=('Roboto', 36))
        # self.sad_button = tk.Button(self.parent_frame, text="😥", font=('Roboto', 36))
        # self.crying_button = tk.Button(self.parent_frame, text="😭", font=('Roboto', 36))
        # self.mood_label = ttk.Label(self.parent_frame, text="Mood:", font=('Roboto', 32), anchor='center', background="#eff5f6")
        # self.mood_value_label = ttk.Label(self.parent_frame, text="", font=('Roboto', 32), anchor='center', background='#eff5f6')
        # self.setup_layout()

    # def setup_layout(self):
    #     self.happy_button.place(x=233, y=300, anchor='center')
    #     self.slightly_happy_button.place(x=433, y=300, anchor='center')
    #     self.sad_button.place(x=633, y=300, anchor='center')
    #     self.crying_button.place(x=833, y=300, anchor='center')
    #     self.mood_label.place(x=380, y=400, anchor='center')
    #     self.mood_value_label.place(x=600, y=400, anchor='center')
    #     # self.save_mood_button.place(x=600, y=500, anchor='center')
    #     # self.update_mood_value_label()

    def destroy(self):
        self.parent_frame.destroy()