from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

import helper

class Dashboard:
    def __init__(self, window):
        self.window = window
        self.window.title('Dashboard - Serenity')
        self.window.geometry(helper.geometry)
        self.window.resizable(0, 0)
        self.window.config(background='#eff5f6')
        icon = PhotoImage(file='assets/dashboard/pic-icon.png')
        self.window.iconphoto(True, icon)
        self.window.protocol('WM_DELETE_WINDOW', self.Exit)

        self.current_frame = None  # To keep track of the current frame being displayed

        # HEADER
        self.header = Frame(self.window, bg=helper.primaryColor)
        self.header.place(x=300, y=0, width=1070, height=60)

        self.headerText = Label(self.header, text="Dashboard", bg=helper.primaryColor, font=("", 20, "bold"))
        self.headerText.place(x=5, y=12)

        self.logout_text = Button(self.header, text='Logout', bg=helper.accentColor, font=("", 13, "bold"), bd=0, fg='white',
                                  cursor='hand2', activebackground='#32cf8e', command=self.Exit)
        self.logout_text.place(x=980, y=15)

        # SIDEBAR
        self.sidebar = Frame(self.window, bg='#ffffff')
        self.sidebar.place(x=0, y=0, width=300, height=768)

        self.create_sidebar()

        # BODY
        self.body = Frame(self.window, bg='#eff5f6')
        self.body.place(x=300, y=60, width=1040, height=655)

        # Initialize with the Dashboard frame
        self.show_dashboard()

    def create_sidebar(self):
        # Logo
        self.logoImage = Image.open('assets/dashboard/hyy.png')
        photo = ImageTk.PhotoImage(self.logoImage)
        self.logo = Label(self.sidebar, image=photo, bg='#ffffff')
        self.logo.image = photo
        self.logo.place(x=70, y=80)

        # Name of brand/person
        self.brandName = Label(self.sidebar, text='Hello Hooman', bg='#ffffff', font=("", 15, "bold"))
        self.brandName.place(x=80, y=200)

        # Dashboard
        self.dashboardImage = Image.open('assets/dashboard/dashboard-icon.png')
        photo = ImageTk.PhotoImage(self.dashboardImage)
        self.dashboard = Label(self.sidebar, image=photo, bg='#ffffff')
        self.dashboard.image = photo
        self.dashboard.place(x=35, y=289)

        self.dashboard_text = Button(self.sidebar, text='Dashboard', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                     cursor='hand2', activebackground='#ffffff', command=self.show_dashboard)
        self.dashboard_text.place(x=80, y=291)

        # Stress Test
        self.stresstestImage = Image.open('assets/dashboard/manage-icon.png')
        photo = ImageTk.PhotoImage(self.stresstestImage)
        self.stresstest = Label(self.sidebar, image=photo, bg='#ffffff')
        self.stresstest.image = photo
        self.stresstest.place(x=35, y=340)

        self.stresstest_text = Button(self.sidebar, text='Stress Test', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='#ffffff', command=self.show_stresstest)
        self.stresstest_text.place(x=80, y=345)

        # Settings
        self.settingsImage = Image.open('assets/dashboard/settings-icon.png')
        photo = ImageTk.PhotoImage(self.settingsImage)
        self.settings = Label(self.sidebar, image=photo, bg='#ffffff')
        self.settings.image = photo
        self.settings.place(x=35, y=402)

        self.settings_text = Button(self.sidebar, text='Settings', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff', command=self.show_settings)
        self.settings_text.place(x=80, y=402)

        # Exit
        self.exitImage = Image.open('assets/dashboard/exit-icon.png')
        photo = ImageTk.PhotoImage(self.exitImage)
        self.exit = Label(self.sidebar, image=photo, bg='#ffffff')
        self.exit.image = photo
        self.exit.place(x=25, y=452)

        self.exit_text = Button(self.sidebar, text='Exit', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                cursor='hand2', activebackground='#ffffff', command=self.Exit)
        self.exit_text.place(x=85, y=462)

    def show_dashboard(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
            self.headerText.config(text="Dashboard")
        self.current_frame = self.create_dashboard_frame()

    def show_stresstest(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
            self.headerText.config(text="Stress Test")
        self.current_frame = self.create_stresstest_frame()

    def show_settings(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
            self.headerText.config(text="Settings")
        self.current_frame = self.create_settings_frame()

    def create_dashboard_frame(self):
        frame = Frame(self.body, bg='#eff5f6')
        frame.place(x=0, y=0, width=1040, height=655)

        # Your Dashboard content creation code here

        # HEADER
        # self.heading = Label(frame, text='Dashboard', font=("", 13, "bold"), fg='#0064d3', bg='#eff5f6')
        # self.heading.place(x=0, y=0)

        # PIE CHART
        data = pd.read_excel("assets/Book1.xlsx")
        sumjulius = sum(data['Julius'])
        sumgideons = sum(data['Gideons'])
        sumjustice = sum(data['Justice'])
        sumdaniel = sum(data['Daniel'])
        sumsimon = sum(data['Simon'])
        sumdennis = sum(data['Dennis'])

        fig = plt.figure(figsize=(5, 3.5), dpi=100)
        fig.set_size_inches(5, 3.5)

        labels = 'Julius', 'Gideons', 'Justice', 'Daniel', 'Simon', 'Dennis'
        sizes = [sumjulius, sumgideons, sumjustice, sumdaniel, sumsimon, sumdennis]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'Orange', 'red']
        explode = (0.2, 0, 0, 0, 0, 0)

        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=550, y=200, anchor=W)

        # BAR CHART
        fig = plt.figure(figsize=(5, 3.5), dpi=100)
        labels = ('Julius', 'Gideons', 'Justice', 'Daniel', 'Simon', 'Dennis')
        labelpos = np.arange(len(labels))
        studentsum = [sumjulius, sumgideons, sumjustice, sumdaniel, sumsimon, sumdennis]

        plt.bar(labelpos, studentsum, align='center', alpha=1.0)
        plt.xticks(labelpos, labels)
        plt.ylabel('Average raw mark')
        plt.xlabel('Students')
        plt.tight_layout(pad=2.2, w_pad=0.5, h_pad=0.1)
        plt.title('Average raw mark for all subjects')
        plt.xticks(rotation=30, horizontalalignment="center")

        for index, datapoints in enumerate(studentsum):
            plt.text(x=index, y=datapoints + 0.3, s=f"{datapoints}", fontdict=dict(fontsize=10), ha='center', va='bottom')

        canvasbar = FigureCanvasTkAgg(fig, master=frame)
        canvasbar.draw()
        canvasbar.get_tk_widget().place(x=20, y=200, anchor=W)

        return frame

    def create_stresstest_frame(self):
        frame = Frame(self.body, bg='#eff5f6')
        frame.place(x=0, y=0, width=1040, height=655)

        # Your Dashboard content creation code here

        # HEADER
        # self.heading = Label(frame, text='Stress Test', font=("", 13, "bold"), fg='#0064d3', bg='#eff5f6')
        # self.heading.place(x=0, y=0)

        # BODY FRAME 1
        self.bodyFrame1 = Frame(frame, bg='#ffffff')
        self.bodyFrame1.place(x=0, y=0, width=1040, height=350)

        # YOUR CODE FOR BODY FRAME 1 HERE

        return frame

    def create_settings_frame(self):
        frame = Frame(self.body, bg='#eff5f6')
        frame.place(x=0, y=0, width=1040, height=655)

        # Your Dashboard content creation code here

        # HEADER
        # self.heading = Label(frame, text='Settings', font=("", 13, "bold"), fg='#0064d3', bg='#eff5f6')
        # self.heading.place(x=0, y=0)

        # BODY FRAME 1
        self.bodyFrame1 = Frame(frame, bg='#ffffff')
        self.bodyFrame1.place(x=10, y=110, width=1040, height=350)

        # YOUR CODE FOR BODY FRAME 1 HERE

        return frame

    def Exit(self):
        if messagebox.askyesno("Quit", " Leave App?") == True:
            self.window.quit()
            exit(0)

    def win():
        window = Tk()
        Dashboard(window)
        window.mainloop()

    # if __name__ == '__main__':
    #     win()
