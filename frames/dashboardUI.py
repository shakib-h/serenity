import os
import tkinter as tk
from tkinter import W, ttk
from PIL import Image, ImageTk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector
import helper

class DashboardUI:
    def __init__(self, parent_frame, username):
        self.parent_frame = parent_frame

        # Connect to your MySQL database
        conn = mysql.connector.connect(**helper.db_config)
        cursor = conn.cursor()

        query = f"SELECT mood FROM mood_data WHERE user='{username}'"
        cursor.execute(query)
        data = cursor.fetchall()

        # Create a DataFrame from the fetched data
        mood_df = pd.DataFrame(data, columns=['mood'])

        # Generate pie chart
        fig = plt.figure(figsize=(5, 3.5), dpi=100)
        fig.set_size_inches(5, 3.5)

        # Count the occurrences of each mood
        mood_counts = mood_df['mood'].value_counts()

        labels = mood_counts.index
        sizes = mood_counts.values
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
        # explode = (0, 0, 0, 0)

        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.title('Mood Over Time')
        plt.axis('equal')

        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=550, y=200, anchor=W)


        # Query MySQL to get the data for the specified user
        query = f"SELECT stress_level, date FROM stress_results WHERE user='{username}'"
        cursor.execute(query)
        data = cursor.fetchall()

        # Separate data into date and stress_level
        stress_levels = [row[0] for row in data]
        dates = [row[1] for row in data]

        # Create a bar chart
        fig = plt.figure(figsize=(5, 3.5), dpi=100)
        labelpos = np.arange(len(dates))

        plt.bar(labelpos, stress_levels, align='center', alpha=1.0)
        plt.xticks(labelpos, dates)
        plt.title('Stress Level')
        plt.xticks(rotation=0, horizontalalignment="center")

        # Set y-axis limits to 0 and 100
        plt.ylim(0, 100)

        for index, datapoint in enumerate(stress_levels):
            plt.text(x=index, y=datapoint, s=f"{datapoint}", fontdict=dict(fontsize=10), ha='center', va='bottom')
        canvasbar = FigureCanvasTkAgg(fig, master=parent_frame)
        canvasbar.draw()
        canvasbar.get_tk_widget().place(x=20, y=200, anchor=W)

        # Create labels for displaying quotes
        self.quote_label = tk.Label(parent_frame, text="", font=('Impact', 32), wraplength=700, background="#eff5f6")
        self.quote_author = tk.Label(parent_frame, text="", font=('Helvetica', 15), wraplength=500, background="#eff5f6")
        self.quote_label.place(x=200, y=500, anchor=W)
        self.quote_author.place(x=700, y=600, anchor=W)

        # Initial quote
        self.update_quote()

    def update_quote(self):
        # Read quotes from the "quote.txt" file
        quotes_path = os.path.join(helper.parent_directory, "serenity", "assets", "quotes.txt")
        with open(quotes_path, "r") as file:
            quotes = [line.strip() for line in file]

        if hasattr(self, "current_quote_index"):
            self.current_quote_index = (self.current_quote_index + 1) % len(quotes)
        else:
            self.current_quote_index = 0

        # Extract author and quote
        quote_line = quotes[self.current_quote_index].split(',')
        author, quote = quote_line[0], quote_line[1]

        # Format the quote with author
        formatted_quote = f"{quote}"
        formatted_author = f"- {author}"

        # Display the current formatted quote
        self.quote_label.config(text=formatted_quote)
        self.quote_author.config(text=formatted_author)

        # Schedule the next update after 15 seconds
        self.parent_frame.after(15000, self.update_quote)

    def destroy(self):
        self.parent_frame.destroy()