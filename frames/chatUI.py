import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from openai import OpenAI
import helper

client = OpenAI(
  api_key=helper.api_key,  # this is also the default, it can be omitted
)

xi = 20
yi = 20

class ChatUI:
    def __init__(self, parent_frame, displayname):
        self.parent_frames = parent_frame
        self.displayname = displayname
        image_path = os.path.join(helper.parent_directory, "serenity", "assets", "sendButton.png")
        self.send_image = ImageTk.PhotoImage(file=image_path)

        # Declare user and bot_response labels as instance variables
        self.user_message = None
        self.bot_response_label = None
        self.bot_response_text = None

        self.serenity_ui()

    def serenity_ui(self):
        # chat bg
        chat_bg = ttk.Frame(self.parent_frames, height=580, width=1040, style="TFrame")
        chat_bg.place(x=10, y=10)

        # entry bg
        entry_bg = ttk.Frame(self.parent_frames, height=60, width=950, style="TFrame")
        entry_bg.place(x=10, y=600)

        # send button
        snd_btn = ttk.Frame(self.parent_frames, height="60", width="65", style="TFrame")
        snd_btn.place(x=970, y=600)
        send_button = tk.Button(snd_btn, bg="#ffffff", image=self.send_image, command=self.send_message)
        send_button.place(x=-1, y=-3)

        # user entry
        self.user_entry = tk.Entry(entry_bg, width="62", bg="White", font=("Helvetica", 20), relief="flat", border=0)
        self.user_entry.place(x=10, y=13)
        self.user_entry.insert(0, "Enter message...")
        self.user_entry.config(fg="#325343")
        self.user_entry.bind("<FocusIn>", self.on_entry)
        self.user_entry.bind("<FocusOut>", self.on_leave)
        self.user_entry.bind("<Return>", lambda event=None: self.send_message())

        # Create user label
        self.user_message = ttk.Label(self.parent_frames, style="RoundedRect.TLabel", text="", anchor="e", font=("Helvetica", 20))
        self.user_message.place(x=xi, y=yi)

        # Create bot_response labels
        self.bot_response_label = ttk.Label(self.parent_frames, style="RoundedRect.TLabel", text="", anchor="w", font=("Helvetica", 20), wraplength=900)
        self.bot_response_label.place(x=xi, y=yi + 45)

        self.bot_response_text = ttk.Label(self.parent_frames, style="RoundedRect.TLabel", text="", anchor="w", font=("Helvetica", 20), wraplength=900)
        self.bot_response_text.place(x=xi + 120, y=yi + 45)

    def send_message(self):
        global yi
        user_input = self.user_entry.get()

        if user_input:
            
            prompt = "This app is for mental health support. You are now chatting with Serenity, a mental health support bot. User: " + user_input


            response = client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=f"The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nYou: {user_input}\nSerenity: I am an AI created by OpenAI. How can I help you today?\nYo: I need help with mental health\nSerenity:",
                temperature=0.9,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=[f" {self.displayname}:", " Serenity:"]
            )

            bot_response = response.choices[0].text


            self.user_message.config(text=f"{self.displayname}: " + user_input)


            self.bot_response_label.config(text="Serenity: ", anchor="w", wraplength=900)
            self.bot_response_text.config(text=bot_response, anchor="w", wraplength=900)


        else:
            
            self.bot_response_label.config(text="Serenity: Enter a message", anchor="w")


        self.user_entry.delete(0, "end")

    def on_entry(self, e):
        self.user_entry.delete(0, "end")
        self.user_entry.config(bg="#ffffff")

    def on_leave(self, e):
        n = self.user_entry.get()
        self.user_entry.config(fg="#325343")

        if n == " " or n == ' ':
            self.user_entry.insert(0, "Enter message...")
        self.user_entry.config(fg="#325343")

    def destroy(self):
        self.parent_frames.destroy()
