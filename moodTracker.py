import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class MoodTracker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Mood Tracker")
        self.window.geometry("1280x720") # Set the window size to 16:9 ratio.

        # Create the background image.
        self.background_image = Image.open("C:/Users/User/Downloads/wp7225545-desktop-one-piece-wano-wallpapers.jpg")
        self.background_image = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self.window, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Add label for user's feeling.
        self.feeling_label = ttk.Label(self.window, text="How are you feeling today?", font=('Arial', 30), anchor='center')
        self.feeling_label.place(x=840, y=150, anchor='center')

        # Create the emoji buttons with larger font size.
        button_font = ('Arial', 36)  # Adjust the font size as needed
        self.happy_button = tk.Button(self.window, text="😁", command=self.happy_mood, font=button_font)
        self.slightly_happy_button = tk.Button(self.window, text="🙁", command=self.slightly_happy_mood, font=button_font)
        self.sad_button = tk.Button(self.window, text="😥", command=self.sad_mood, font=button_font)
        self.crying_button = tk.Button(self.window, text="😭", command=self.crying_mood, font=button_font)

        # Create the mood label with larger font size.
        mood_label_font = ('Arial', 48)  # Adjust the font size as needed
        self.mood_label = ttk.Label(self.window, text="Mood:", font=mood_label_font, anchor='center')

        # Create the mood value label with larger font size.
        mood_value_label_font = ('Arial', 48)  # Adjust the font size as needed
        self.mood_value_label = ttk.Label(self.window, text="0%", font=mood_value_label_font, anchor='center')

        # Layout the widgets.
        self.happy_button.place(x=540, y=300, anchor='center')
        self.slightly_happy_button.place(x=740, y=300, anchor='center')
        self.sad_button.place(x=940, y=300, anchor='center')
        self.crying_button.place(x=1140, y=300, anchor='center')
        self.mood_label.place(x=650, y=400, anchor='center')
        self.mood_value_label.place(x=900, y=400, anchor='center')

        # Initialize the mood value.
        self.mood_value = 0

        # Start the main loop.
        self.window.mainloop()

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

if __name__ == "__main__":
    MoodTracker()
