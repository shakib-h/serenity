# importing library
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
import time
import helper


class Splash:


    w = Tk()

    width_of_window = 427
    height_of_window = 250
    screen_width = w.winfo_screenwidth()
    screen_height = w.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    w.geometry("%dx%d+%d+%d" %
            (width_of_window, height_of_window, x_coordinate, y_coordinate))
    
    w.overrideredirect(1) 

    Frame(w, width=427, height=250, bg=helper.accentColor).place(x=0, y=0)
    label1 = Label(w, text='SERENITY', fg='white',
                bg=helper.accentColor)  # decorate it
    # You need to install this font in your PC or try another one
    label1.configure(font=("Game Of Squids", 24, "bold"))
    label1.place(x=135, y=90)

    label2 = Label(w, text='Loading...', fg='white',
                bg=helper.accentColor)  # decorate it
    label2.configure(font=("Calibri", 11))
    label2.place(x=10, y=215)


    image_a = ImageTk.PhotoImage(Image.open('assets/splash/c2.png'))
    image_b = ImageTk.PhotoImage(Image.open('assets/splash/c1.png'))


    for i in range(2): 
        l1 = Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
        l2 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
        l3 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
        l4 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
        w.update_idletasks()
        time.sleep(0.5)

        l1 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
        l2 = Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
        l3 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
        l4 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
        w.update_idletasks()
        time.sleep(0.5)

        l1 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
        l2 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
        l3 = Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
        l4 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
        w.update_idletasks()
        time.sleep(0.5)

        l1 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
        l2 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
        l3 = Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
        l4 = Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
        w.update_idletasks()
        time.sleep(0.5)


    w.destroy()
