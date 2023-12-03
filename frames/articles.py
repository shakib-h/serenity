import threading
import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk
import requests
from io import BytesIO

blogs = [
     {"title": "Do I Even Need Counseling?", "link": "https://www.betterhelp.com/advice/counseling/do-i-even-need-counseling-the-unique-expansiveness-of-psychotherapy/", "image_url": "https://dz9yg0snnohlc.cloudfront.net/advice/images/betterhelp/7563/43cc4eaab49e5d5f0bf9c8752ed9d9f7-man-stressed-headphones-white-shirt_l_sm.jpg"},
    {"title": "Is It Time To Start Therapy?", "link": "https://www.betterhelp.com/advice/therapy/is-it-time-to-start-therapy-why-you-shouldnt-procrastinate-on-mental-health/", "image_url": "https://dz9yg0snnohlc.cloudfront.net/advice/images/betterhelp/7564/3888fff2403ef88711369f831050b77f-man-in-yellow-shirt-stressed-on-couch_l_sm.jpg"},
    {"title": "Is It Okay To Pause Therapy?", "link": "https://www.betterhelp.com/advice/therapy/is-it-okay-to-pause-therapy-understanding-the-risks-and-benefits/", "image_url": "https://dz9yg0snnohlc.cloudfront.net/advice/images/betterhelp/7565/9c4411b96b467ea1b2b210b689b27ff2-man-looks-stressed-while-typing-on-laptop_l_sm.jpeg"},
    {"title": "Anxiety Therapy For Teenagers", "link": "https://www.betterhelp.com/advice/anxiety/anxiety-therapy-for-teenagers-choosing-the-right-treatment/", "image_url": "https://dz9yg0snnohlc.cloudfront.net/advice/images/betterhelp/7436/104c67616738e47ab05186afc33cbf2c-mom-and-daughter-on-phone-girl-in-yellow-sweater_l_xsm.jpeg"},
    {"title": "Finding The Best Local Therapist", "link": "https://www.betterhelp.com/advice/therapy/how-do-i-find-a-therapist-near-me/", "image_url": "https://dz9yg0snnohlc.cloudfront.net/advice/images/betterhelp/310/363b09cfa9f275639872fb6d3fcc7df9-couple-on-the-couch-smiling_sm.jpeg"},
    {"title": "Effectiveness Of Art Therapy", "link": "https://www.betterhelp.com/advice/therapy/effectiveness-of-art-therapy-the-role-of-art-therapy-for-mental-health/", "image_url": "https://dz9yg0snnohlc.cloudfront.net/advice/images/betterhelp/7569/41793fbbd9726ade8de735f90be0340d-elderly-man-works-pottery_l_xsm.jpg"},
]

class BlogPage:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        
        # Create a custom style for rounded rectangular labels
        style = ttk.Style()
        style.configure("RoundedRect.TLabel", borderwidth=1, relief="solid", padding=10, background="white",
                        bordercolor="gray", borderradius=10)

        # Create a canvas with a vertical scrollbar
        self.canvas = tk.Canvas(self.parent_frame, borderwidth=0)
        vsb = tk.Scrollbar(self.parent_frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=vsb.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")

        self.frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.frame.bind("<Configure>", lambda event, canvas=self.canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        # Function to handle mouse wheel scrolling
        def on_mousewheel(event):
            self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

        # Bind mouse wheel scrolling to the canvas
        self.canvas.bind_all("<MouseWheel>", on_mousewheel)

        # Calculate the width of the link boxes based on the window size
        box_width = 470  # Half the window width
        box_height = 300  # You can adjust this value as needed

        # Create two frames, one for each column
        self.frame1 = ttk.Frame(self.frame)
        self.frame2 = ttk.Frame(self.frame)
        self.frame1.grid(row=0, column=0, sticky="nsew")
        self.frame2.grid(row=0, column=1, sticky="nsew")

        # Create labels for each blog entry with images resized to the calculated box size
        for i, blog in enumerate(blogs):
            title = blog["title"]
            link = blog["link"]
            image_url = blog["image_url"]

            # Create a placeholder image
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

            # Load the actual image after a delay
            self.load_image_after_delay(label, image_url, box_width, box_height)

            label.bind("<Button-1>", lambda event, link=link: self.open_link(link))

        # Configure row and column weights for grid resizing
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

    def open_link(self, link):
        webbrowser.open(link)

    def load_image_after_delay(self, label, image_url, width, height):
        # Define a function to load the image and update the label
        def load_image_and_update_label():
            try:
                response = requests.get(image_url)
                img = Image.open(BytesIO(response.content))
                img = img.resize((width, height), Image.LANCZOS)  # Resize the image
                photo = ImageTk.PhotoImage(img)

                # Update the label with the loaded image
                label.config(image=photo)
                label.image = photo

            except Exception as e:
                print(f"Error loading image: {e}")

        # Schedule the image loading function after a delay using threading
        thread = threading.Thread(target=load_image_and_update_label)
        thread.start()

    def destroy(self):
        self.parent_frame.destroy()