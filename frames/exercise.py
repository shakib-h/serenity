import threading
import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk
import requests
from io import BytesIO

exercises = [
     {"title": "4 Ways to Have Good Mental Health", "link": "https://www.wikihow.com/Have-Good-Mental-Health", "image_url": "https://www.wikihow.com/images/thumb/1/1a/Have-Good-Mental-Health-Step-6-Version-4.jpg/v4-460px-Have-Good-Mental-Health-Step-6-Version-4.jpg"},
    {"title": "How to Increase Mental Strength", "link": "https://www.wikihow.com/Increase-Mental-Strength", "image_url": "https://www.wikihow.com/images/thumb/b/ba/Have-Good-Mental-Health-Step-5-Version-4.jpg/v4-460px-Have-Good-Mental-Health-Step-5-Version-4.jpg"},
    {"title": "How to Take a Mental Health Day", "link": "https://www.wikihow.com/Take-a-Mental-Health-Day-Without-Feeling-Guilty", "image_url": "https://www.wikihow.com/images/thumb/d/db/Take-a-Mental-Health-Day-Without-Feeling-Guilty-Step-2-Version-3.jpg/v4-460px-Take-a-Mental-Health-Day-Without-Feeling-Guilty-Step-2-Version-3.jpg"},
]

class Exercise:
    def __init__(self, parent_frame, username):
        self.parent_frame = parent_frame
        self.username = username
        
        style = ttk.Style()
        style.configure("RoundedRect.TLabel", borderwidth=1, relief="solid", padding=10, background="white",
                        bordercolor="gray", borderradius=10)


        self.canvas = tk.Canvas(self.parent_frame, borderwidth=0)
        vsb = tk.Scrollbar(self.parent_frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=vsb.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")

        self.frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.frame.bind("<Configure>", lambda event, canvas=self.canvas: canvas.configure(scrollregion=canvas.bbox("all")))


        def on_mousewheel(event):
            self.canvas.yview_scroll(-1 * (event.delta // 120), "units")


        self.canvas.bind_all("<MouseWheel>", on_mousewheel)

        box_width = 470 
        box_height = 300

        self.frame1 = ttk.Frame(self.frame)
        self.frame2 = ttk.Frame(self.frame)
        self.frame1.grid(row=0, column=0, sticky="nsew")
        self.frame2.grid(row=0, column=1, sticky="nsew")

        for i, blog in enumerate(exercises):
            title = blog["title"]
            link = blog["link"]
            image_url = blog["image_url"]

            placeholder_img = Image.new("RGB", (box_width, box_height), "white")
            placeholder_photo = ImageTk.PhotoImage(placeholder_img)

            target_frame = self.frame1 if i % 2 == 0 else self.frame2

            label = ttk.Label(
                target_frame,
                text=title,
                image=placeholder_photo,
                compound="top",
                cursor="hand2",
                style="RoundedRect.TLabel",
                font=("Helvetica", 12),
            )
            label.image = placeholder_photo
            label.grid(row=i // 2, padx=10, pady=10, sticky="nsew")

            self.load_image_after_delay(label, image_url, box_width, box_height)

            label.bind("<Button-1>", lambda event, link=link: self.open_link(link))

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

    def open_link(self, link):
        webbrowser.open(link)

    def load_image_after_delay(self, label, image_url, width, height):
        def load_image_and_update_label():
            try:
                response = requests.get(image_url)
                img = Image.open(BytesIO(response.content))
                img = img.resize((width, height), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)


                label.config(image=photo)
                label.image = photo

            except Exception as e:
                print(f"Error loading image: {e}")


        thread = threading.Thread(target=load_image_and_update_label)
        thread.start()

    def destroy(self):
        self.parent_frame.destroy()