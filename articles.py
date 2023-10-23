import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Create the main window
window = tk.Tk()
window.title("Modern Blog Page")

# Define a modern font
modern_font = ("Helvetica", 12)

# Create a canvas for the entire page content
canvas = tk.Canvas(window)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar for the canvas
scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.config(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas for the articles
content_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Sample blog content with online image URLs
blog_content = [
    {
        "title": "First Post",
        "content": "This is my first blog post. It's all about the beginning of my journey.",
        "link": "https://www.example.com/post1",
        "image_url": "https://images.unsplash.com/photo-1682687220866-c856f566f1bd?auto=format&fit=crop&q=80&w=2670&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8M",
    },
    {
        "title": "Second Post",
        "content": "Here's the second post on my blog. Learn about my latest adventures.",
        "link": "https://www.example.com/post2",
        "image_url": "https://images.unsplash.com/photo-1682687220866-c856f566f1bd?auto=format&fit=crop&q=80&w=2670&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8M",
    },
    {
        "title": "Third Post",
        "content": "And this is the third one. Discover exciting stories and more.",
        "link": "https://www.example.com/post3",
        "image_url": "https://images.unsplash.com/photo-1682687220866-c856f566f1bd?auto=format&fit=crop&q=80&w=2670&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8M",
    },
]

# Function to open the link
def open_link(link):
    import webbrowser
    webbrowser.open(link)

# Function to handle the click event
def handle_click(event, link):
    open_link(link)

# Function to change cursor on hover
def change_cursor(event):
    event.widget.config(cursor="hand2")

# Function to display the online image with full width
def display_image(image_url, frame):
    response = requests.get(image_url)
    img_data = BytesIO(response.content)
    img = Image.open(img_data)
    img = img.resize((600, 400), Image.LANCZOS)  # Set the size for full width
    img = ImageTk.PhotoImage(img)
    image_label = ttk.Label(frame, image=img)
    image_label.image = img  # To prevent the image from being garbage collected
    image_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="w")

# Create labels and frames for the blog posts
for i, post in enumerate(blog_content):
    post_frame = ttk.Frame(content_frame, relief=tk.SOLID, borderwidth=2)
    row, col = divmod(i, 2)  # Arrange two articles side by side
    post_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

    # Display the online image with full width
    display_image(post["image_url"], post_frame)

    post_title = ttk.Label(post_frame, text=post["title"], font=("Helvetica", 18, "bold"))
    post_title.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    post_text = ttk.Label(post_frame, text=post["content"], font=modern_font, wraplength=600, justify="left")
    post_text.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    # Bind the click event to open the link
    post_frame.bind("<Button-1>", lambda event, link=post["link"]: handle_click(event, link))
    
    # Change the cursor to a pointer on hover
    post_frame.bind("<Enter>", change_cursor)
    post_frame.bind("<Leave>", lambda event: event.widget.config(cursor=""))

    # Configure grid weights
    post_frame.columnconfigure(0, weight=1)
    post_frame.rowconfigure(2, weight=1)

# Update the canvas to fit the content
content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Run the main loop
window.mainloop()