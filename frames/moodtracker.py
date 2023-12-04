from datetime import datetime
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import helper

class MoodTracker:
    def __init__(self, parent_frame, username):
        self.parent_frame = parent_frame
        self.username = username
        self.mood_value = ""
        self.create_or_check_tables()
        self.happy_button = tk.Button(self.parent_frame, text="😁", command=self.happy_mood, font=('Roboto', 36))
        self.slightly_happy_button = tk.Button(self.parent_frame, text="🙁", command=self.slightly_happy_mood, font=('Roboto', 36))
        self.sad_button = tk.Button(self.parent_frame, text="😥", command=self.sad_mood, font=('Roboto', 36))
        self.crying_button = tk.Button(self.parent_frame, text="😭", command=self.crying_mood, font=('Roboto', 36))
        self.mood_label = ttk.Label(self.parent_frame, text="Mood:", font=('Roboto', 32), anchor='center', background="#eff5f6")
        self.mood_value_label = ttk.Label(self.parent_frame, text="", font=('Roboto', 32), anchor='center', background='#eff5f6')
        self.mood_label_help = ttk.Label(self.parent_frame, text="", font=('Roboto', 22), anchor='center', background="#eff5f6")
        self.setup_layout()

    def create_or_check_tables(self):
        base = mysql.connector.connect(**helper.db_config)
        cur = base.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS mood_data ("
                    "id INT AUTO_INCREMENT PRIMARY KEY, mood INT, user VARCHAR(20), "
                    "date DATE, time TIME, FOREIGN KEY (user) REFERENCES users(username));")
        base.commit()
        base.close()

    def setup_layout(self):
        self.happy_button.place(x=233, y=300, anchor='center')
        self.slightly_happy_button.place(x=433, y=300, anchor='center')
        self.sad_button.place(x=633, y=300, anchor='center')
        self.crying_button.place(x=833, y=300, anchor='center')
        self.mood_label.place(x=380, y=400, anchor='center')
        self.mood_value_label.place(x=600, y=400, anchor='center')
        self.mood_label_help.place(x=600, y=500, anchor='center')

    def happy_mood(self):
        self.mood_value = "Happy"
        self.update_mood_value_label()

    def slightly_happy_mood(self):
        self.mood_value = "Neutral"
        self.update_mood_value_label()

    def sad_mood(self):
        self.mood_value = "Sad"
        self.update_mood_value_label()
        self.mood_label_help["text"] = "Please move over to the chatbot for further assistance."

    def crying_mood(self):
        self.mood_value = "Broken"
        self.update_mood_value_label()
        self.mood_label_help["text"] = "Please move over to the chatbot for further assistance."

    def update_mood_value_label(self):
        self.mood_value_label["text"] = f"{self.mood_value}"
        base = mysql.connector.connect(**helper.db_config)
        cur = base.cursor()
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cur.execute("INSERT INTO mood_data (mood, user, date, time) VALUES (%s, %s, %s, %s)",
                    (self.mood_value, self.username, current_datetime.split()[0], current_datetime.split()[1]))
        base.commit()
        base.close()

    def destroy(self):
        self.parent_frame.destroy()