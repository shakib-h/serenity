
import tkinter as tk
import webbrowser

# Sample list of articles with their links
articles = [
    {"title": "Article 1", "link": "https://www.example.com/article1"},
    {"title": "Article 2", "link": "https://www.example.com/article2"},
    {"title": "Article 3", "link": "https://www.example.com/article3"},
   
]

# Function to open a web page in the default browser
def open_link(link):
    webbrowser.open_new(link)

# Function to close the window
def close_window():
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Article Links")
root.geometry("800x600")  # Set a custom window size

# Create a frame with a custom background color
frame = tk.Frame(root, bg="#333333")
frame.pack(fill=tk.BOTH, expand=True)

# Customize the title label
title_label = tk.Label(frame, text="Article Links", fg="white", bg="#333333", font=("Helvetica", 24))
title_label.pack(pady=20)

# Populate the frame with article links
for article in articles:
    link_label = tk.Label(frame, text=article["title"], cursor="hand2", fg="blue", font=("Helvetica", 14))
    link_label.bind("<Button-1>", lambda e, link=article["link"]: open_link(link))
    link_label.pack(pady=10)

# Create a close button with custom style
close_button = tk.Button(frame, text="Close", command=close_window, bg="red", fg="white", font=("Helvetica", 14))
close_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
 
 
 