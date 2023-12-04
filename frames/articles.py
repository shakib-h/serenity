import threading
import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk
import requests
from io import BytesIO

new_blogs = [
     {"new_title": "Do I Even Need Counseling?", "new_link": "https://www.betterhelp.com/advice/counseling/do-i-even-need-counseling-the-unique-expansiveness-of-psychotherapy/", "new_image_url": "https://dz9yg0snnohlc.cloudfront.net/advice/images/betterhelp/7563/43cc4eaab49e5d5f0bf9c8752ed9d9f7-man-stressed-headphones-white-shirt_l_sm.jpg"},
    {"new_title": "Is It Time To Start Therapy?", "new_link": "https://www.betterhelp.com/advice/therapy/is-it-time-to-start-therapy-why-you-shouldnt-procrastinate-on-mental-health/", "new_image_url": "https://dz9yg0snnohlc.cloudfront.net/advice/images/betterhelp/7564/3888fff2403ef88711369f831050b77f-man-in-yellow-shirt-stressed-on-couch_l_sm.jpg"},
    {"new_title": "Is It Okay To Pause Therapy?", "new_link": "https://www.betterhelp.com/advice/therapy/is-it-okay-to-pause-therapy-understanding-the-risks-and-benefits/", "new_image_url": "https://dz9yg0snnohlc.cloudfront.net/advice/images/betterhelp/7565/9c4411b96b467ea1b2b210b689b27ff2-man-looks-stressed-while-typing-on-laptop_l_sm.jpeg"},
    {"new_title": "Anxiety Therapy For Teenagers", "new_link": "https://www.betterhelp.com/advice/anxiety/anxiety-therapy-for-teenagers-choosing-the-right-treatment/", "new_image_url": "https://dz9yg0snnohlc.cloudfront.net/advice/images/betterhelp/7436/104c67616738e47ab05186afc33cbf2c-mom-and-daughter-on-phone-girl-in-yellow-sweater_l_xsm.jpeg"},
    {"new_title": "Finding The Best Local Therapist", "new_link": "https://www.betterhelp.com/advice/therapy/how-do-i-find-a-therapist-near-me/", "new_image_url": "https://dz9yg0snnohlc.cloudfront.net/advice/images/betterhelp/310/363b09cfa9f275639872fb6d3fcc7df9-couple-on-the-couch-smiling_sm.jpeg"},
    {"new_title": "Effectiveness Of Art Therapy", "new_link": "https://www.betterhelp.com/advice/therapy/effectiveness-of-art-therapy-the-role-of-art-therapy-for-mental-health/", "new_image_url": "https://dz9yg0snnohlc.cloudfront.net/advice/images/betterhelp/7569/41793fbbd9726ade8de735f90be0340d-elderly-man-works-pottery_l_xsm.jpg"},
]

class BlogPage:
    def __init__(self, new_parent_frame):
        self.new_parent_frame = new_parent_frame
    
        new_style = ttk.Style()
        new_style.configure("RoundedRect.TLabel", borderwidth=1, relief="solid", padding=10, background="white",
                        bordercolor="gray", borderradius=10)

        self.new_canvas = tk.Canvas(self.new_parent_frame, borderwidth=0)
        vsb = tk.Scrollbar(self.new_parent_frame, orient="vertical", command=self.new_canvas.yview)
        self.new_canvas.configure(yscrollcommand=vsb.set)

        self.new_canvas.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")

        self.new_frame = ttk.Frame(self.new_canvas)
        self.new_canvas.create_window((0, 0), window=self.new_frame, anchor="nw")

        self.new_frame.bind("<Configure>", lambda event, canvas=self.new_canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        def on_mousewheel(event):
            self.new_canvas.yview_scroll(-1 * (event.delta // 120), "units")

        self.new_canvas.bind_all("<MouseWheel>", on_mousewheel)

        new_box_width = 470
        new_box_height = 300


        self.new_frame1 = ttk.Frame(self.new_frame)
        self.new_frame2 = ttk.Frame(self.new_frame)
        self.new_frame1.grid(row=0, column=0, sticky="nsew")
        self.new_frame2.grid(row=0, column=1, sticky="nsew")


        for i, new_blog in enumerate(new_blogs):
            new_title = new_blog["new_title"]
            new_link = new_blog["new_link"]
            new_image_url = new_blog["new_image_url"]

            # Create a placeholder image
            new_placeholder_img = Image.new("RGB", (new_box_width, new_box_height), "white")
            new_placeholder_photo = ImageTk.PhotoImage(new_placeholder_img)

            new_target_frame = self.new_frame1 if i % 2 == 0 else self.new_frame2

            new_label = ttk.Label(
                new_target_frame,
                text=new_title,
                image=new_placeholder_photo,
                compound="top",
                cursor="hand2",
                style="RoundedRect.TLabel",
                font=("Helvetica", 12),
            )
            new_label.image = new_placeholder_photo
            new_label.grid(row=i // 2, padx=10, pady=10, sticky="nsew")

            self.load_image_after_delay(new_label, new_image_url, new_box_width, new_box_height)

            new_label.bind("<Button-1>", lambda event, new_link=new_link: self.open_link(new_link))


        self.new_frame.grid_rowconfigure(0, weight=1)
        self.new_frame.grid_columnconfigure(0, weight=1)
        self.new_frame.grid_columnconfigure(1, weight=1)

    def open_link(self, new_link):
        webbrowser.open(new_link)

    def load_image_after_delay(self, new_label, new_image_url, new_width, new_height):
        def load_image_and_update_label():
            try:
                response = requests.get(new_image_url)
                img = Image.open(BytesIO(response.content))
                img = img.resize((new_width, new_height), Image.LANCZOS)
                new_photo = ImageTk.PhotoImage(img)


                new_label.config(image=new_photo)
                new_label.image = new_photo

            except Exception as e:
                print(f"Error loading image: {e}")

        thread = threading.Thread(target=load_image_and_update_label)
        thread.start()

    def destroy(self):
        self.new_parent_frame.destroy()
