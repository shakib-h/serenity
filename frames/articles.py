import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk
import requests
from io import BytesIO

blogs = [
     {"title": "Blog 1", "link": "https://example.com/blog1", "image_url": "https://images.unsplash.com/photo-1614517453351-6c1522fc7a56?auto=format&fit=crop&q=80&w=380"},
    {"title": "Blog 1", "link": "https://example.com/blog1", "image_url": "https://images.unsplash.com/photo-1614517453351-6c1522fc7a56?auto=format&fit=crop&q=80&w=380"},
    {"title": "Blog 1", "link": "https://example.com/blog1", "image_url": "https://images.unsplash.com/photo-1614517453351-6c1522fc7a56?auto=format&fit=crop&q=80&w=380"},
    {"title": "Blog 1", "link": "https://example.com/blog1", "image_url": "https://images.unsplash.com/photo-1614517453351-6c1522fc7a56?auto=format&fit=crop&q=80&w=380"},
    {"title": "Blog 1", "link": "https://example.com/blog1", "image_url": "https://images.unsplash.com/photo-1614517453351-6c1522fc7a56?auto=format&fit=crop&q=80&w=380"},
    {"title": "Blog 1", "link": "https://example.com/blog1", "image_url": "https://images.unsplash.com/photo-1614517453351-6c1522fc7a56?auto=format&fit=crop&q=80&w=380"},
    {"title": "Blog 1", "link": "https://example.com/blog1", "image_url": "https://images.unsplash.com/photo-1614517453351-6c1522fc7a56?auto=format&fit=crop&q=80&w=380"},
]

class BlogPage:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.mood_value = 0

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

            photo = self.load_image(image_url, box_width, box_height)
            if photo:
                target_frame = self.frame1 if i % 2 == 0 else self.frame2

                label = ttk.Label(
                    target_frame,
                    text=title,
                    image=photo,
                    compound="top",
                    cursor="hand2",
                    style="RoundedRect.TLabel"
                )
                label.image = photo
                label.grid(row=i // 2, padx=10, pady=10, sticky="nsew")

                label.bind("<Button-1>", lambda event, link=link: self.open_link(link))

        # Configure row and column weights for grid resizing
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

    def open_link(self, link):
        webbrowser.open(link)

    def load_image(self, image_url, width, height):
        try:
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            img = img.resize((width, height), Image.LANCZOS)  # Resize the image
            photo = ImageTk.PhotoImage(img)
            return photo
        except Exception as e:
            print(f"Error loading image: {e}")
            return None


    def destroy(self):
        self.parent_frame.destroy()