import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os
import openai
import helper

openai.api_key = helper.api_key
xi = 0
yi = 0

# reply from serenity
def send_message():
    global yi
    user_input = user_entry.get()
    
    if user_input:
        # Include a prompt indicating that the app is for mental health support
        prompt = "This app is for mental health support. You are now chatting with Serenity, a mental health support bot. User: " + user_input
        
        # Send the prompt to the ChatGPT API (GPT-3.5-turbo engine)
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\You: Hello, who are you?\nSerenity: I am an AI created by OpenAI. How can I help you today?\nYo: I need help with mental health\nSerenity:",
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" You:", " Serenity:"]
        )

        bot_response = response.choices[0].text
        user = Label(chat_bg, height=1, width=64, bg="#a6de9b", fg="#325343", text="You: " + user_input, font=20, anchor="e")
        user.place(x=xi, y=yi)
        
        # Display the bot's response with word wrapping
        bot_response_label = Label(chat_bg, height=1, width=64, bg="#a6de9b", fg="#325343", font=20, anchor="w", text="Serenity: ")
        bot_response_label.place(x=xi, y=yi + 25)
        bot_response_text = Label(chat_bg, height=1, width=64, bg="#a6de9b", fg="#325343", font=20, anchor="w", text=bot_response)
        bot_response_text.place(x=xi + 100, y=yi + 25)
    else:
        bot_response_label = Label(chat_bg, height=1, width=64, bg="#a6de9b", fg="#325343", font=20, anchor="w", text="Serenity: Enter a message")
        bot_response_label.place(x=xi, y=yi + 25)
        
    # Update yi based on the number of lines used for the bot's response
    bot_response_lines = bot_response.count('\n') + 1
    yi += 50 + (bot_response_lines * 30)

    print(bot_response)


# bg
serenity = Tk()
serenity.title("Serenity")
serenity.geometry("600x600")
serenity.resizable(0, 0)
serenity.configure(bg="#325343")

# heading
heading_txt = Label(height=2, width=14, bg="#325343",
                     text="Serenity", font=("Impact", 20), fg="white")
heading_txt.place(x=5, y=5)

# chat bg
chat_bg = Frame(height=420, width=580, bg="#a6de9b")
chat_bg.place(x=10, y=80)

# entry bg
entry_bg = Frame(height=60, width=500, bg="white")
entry_bg.place(x=10, y=520)

#send button
send = PhotoImage(file="serenity/assets/sendButton.png")
snd_btn = Frame(height="60", width="65", bg="#a6de9b")
snd_btn.place(x=525, y=520)
send_button = Button(snd_btn, bg="#325343", image=send, command=send_message)
send_button.place(x=-1, y=-3)

def on_entry(e):
    user_entry.delete(0, "end")
    user_entry.config(bg="#a6de9b")

def on_leave(e):
    n = user_entry.get()
    user_entry.config(fg="#325343")

    if n == " " or n == ' ':
        user_entry.insert(0, "Enter message...")
    user_entry.config(fg="#325343")

#user entry
user_entry = Entry(entry_bg, width="32", bg="White",
                   font=("Helvectica", 20), relief=FLAT, border=0)
user_entry.place(x=10, y=13)
user_entry.insert(0, "Enter message...")
user_entry.config(fg="#325343")
user_entry.bind("<FocusIn>", on_entry)
user_entry.bind("<FocusOut>", on_leave)

serenity.mainloop()
