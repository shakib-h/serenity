import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Create a list of blog links, titles, and image URLs
blogs = [
    {"title": "Blog 1", "link": "https://example.com/blog1", "image_url": "https://images.unsplash.com/photo-1614517453351-6c1522fc7a56?auto=format&fit=crop&q=80&w=2070&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
    {"title": "Blog 1", "link": "https://example.com/blog1", "image_url": "https://images.unsplash.com/photo-1614517453351-6c1522fc7a56?auto=format&fit=crop&q=80&w=2070&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
    {"title": "Blog 1", "link": "https://example.com/blog1", "image_url": "https://images.unsplash.com/photo-1614517453351-6c1522fc7a56?auto=format&fit=crop&q=80&w=2070&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
    {"title": "Blog 1", "link": "https://example.com/blog1", "image_url": "https://images.unsplash.com/photo-1614517453351-6c1522fc7a56?auto=format&fit=crop&q=80&w=2070&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
    {"title": "Blog 1", "link": "https://example.com/blog1", "image_url": "https://images.unsplash.com/photo-1614517453351-6c1522fc7a56?auto=format&fit=crop&q=80&w=2070&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
    {"title": "Blog 1", "link": "https://example.com/blog1", "image_url": "https://images.unsplash.com/photo-1614517453351-6c1522fc7a56?auto=format&fit=crop&q=80&w=2070&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
    {"title": "Blog 1", "link": "https://example.com/blog1", "image_url": "https://images.unsplash.com/photo-1614517453351-6c1522fc7a56?auto=format&fit=crop&q=80&w=2070&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},

    
]

# Function to open the selected link in a web browser
def open_link(link):
    webbrowser.open(link)

# Function to download and display an image from a URL and resize it
def load_image(image_url, width, height):
    try:
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img = img.resize((width, height), Image.LANCZOS)  # Resize the image
        photo = ImageTk.PhotoImage(img)
        return photo
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

# Create the main window
root = tk.Tk()
root.title("Blog Page")
root.state('zoomed') 

# Create a custom style for rounded rectangular labels
style = ttk.Style()
style.configure("RoundedRect.TLabel", borderwidth=1, relief="solid", padding=10, background="white", bordercolor="gray", borderradius=10)

# Create a canvas with a vertical scrollbar
canvas = tk.Canvas(root, borderwidth=0)
vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

canvas.pack(side="left", fill="both", expand=True)
vsb.pack(side="right", fill="y")

frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

# Function to handle mouse wheel scrolling
def on_mousewheel(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

# Bind mouse wheel scrolling to the canvas
canvas.bind_all("<MouseWheel>", on_mousewheel)

# Calculate the width of the link boxes based on the window size
box_width = root.winfo_screenwidth() // 2  # Half the window width
box_height = 500  # You can adjust this value as needed

# Create two frames, one for each column
frame1 = ttk.Frame(frame)
frame2 = ttk.Frame(frame)
frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=0, column=1, sticky="nsew")

# Create labels for each blog entry with images resized to the calculated box size
for i, blog in enumerate(blogs):
    title = blog["title"]
    link = blog["link"]
    image_url = blog["image_url"]

    photo = load_image(image_url, box_width, box_height)
    if photo:
        if i % 2 == 0:
            target_frame = frame1
        else:
            target_frame = frame2

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

        label.bind("<Button-1>", lambda event, link=link: open_link(link))

# Configure row and column weights for grid resizing
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Run the Tkinter main loop
root.geometry("650x250")  # Set the window size
root.mainloop()