import argparse
import subprocess
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector
from frames.chatUI import ChatUI
from frames.dashboardUI import DashboardUI
from frames.exercise import Exercise
from frames.moodtracker import MoodTracker
from frames.articles import BlogPage
from frames.stresstest import StressTest
import helper

class Dashboard:
    def __init__(self, window):
        parser = argparse.ArgumentParser(description='Dashboard Application')
        parser.add_argument('--username', type=str, help='Username for the dashboard')
        args = parser.parse_args()
        self.username = args.username if args.username else "User"
        self.users_data = self.get_user_data()
        self.displayname = self.users_data['name'] if self.users_data else "User"
        self.window = window
        self.window.title(f'{self.displayname}\'s Dashboard - Serenity')
        self.window.geometry(helper.geometry)
        self.window.resizable(0, 0)
        self.window.config(background='#eff5f6')
        icon = PhotoImage(file='assets/dashboard/pic-icon.png')
        self.window.iconphoto(True, icon)
        self.window.protocol('WM_DELETE_WINDOW', self.Exit)

        self.current_frame = None

        # HEADER
        self.header = Frame(self.window, bg=helper.primaryColor)
        self.header.place(x=300, y=0, width=1070, height=60)

        self.headerText = Label(self.header, text=f"Hello {self.displayname}", bg=helper.primaryColor, font=("", 20, "bold"))

        self.headerText.place(x=5, y=12)

        self.logout_text = Button(self.header, text='Logout', bg=helper.accentColor, font=("", 13, "bold"), bd=0, fg='white',
                                  cursor='hand2', activebackground='#32cf8e', command=self.Logout)
        self.logout_text.place(x=980, y=15)

        # SIDEBAR
        self.sidebar = Frame(self.window, bg='#ffffff')
        self.sidebar.place(x=0, y=0, width=300, height=768)

        self.create_sidebar()

        # BODY
        self.body = Frame(self.window, bg='#eff5f6')
        self.body.place(x=300, y=60, width=1066, height=708)

        # Initializing dashboard frame
        self.show_dashboard()

    def get_user_data(self):
        base = mysql.connector.connect(**helper.db_config)
        cur = base.cursor(dictionary=True) 
        cur.execute("SELECT * FROM users WHERE username = %s", (self.username,))
        result = cur.fetchone()
        base.close()
        return result if result else {}


    def create_sidebar(self):
        # Logo
        self.logoImage = Image.open('assets/dashboard/hyy.png')
        photo = ImageTk.PhotoImage(self.logoImage)
        self.logo = Label(self.sidebar, image=photo, bg='#ffffff')
        self.logo.image = photo
        self.logo.place(x=70, y=80)

        # Name Person
        self.brandName = Label(self.sidebar, text=f'Hello {self.displayname}', bg='#ffffff', font=("", 15, "bold"))
        self.brandName.place(x=80, y=200)

        # Dashboard
        self.dashboardImage = Image.open('assets/dashboard/icons/icons8-calendar-36.png')
        photo = ImageTk.PhotoImage(self.dashboardImage)
        self.dashboard = Label(self.sidebar, image=photo, bg='#ffffff')
        self.dashboard.image = photo
        self.dashboard.grid(row=0, column=0, pady=(280, 0), padx=(35, 0), sticky="w")

        self.dashboard_text = Button(self.sidebar, text='Dashboard', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff', command=self.show_dashboard)
        self.dashboard_text.grid(row=0, column=1, pady=(280, 0), padx=(0, 25), sticky="w")

        # Stress Test
        self.stresstestImage = Image.open('assets/dashboard/icons/icons8-anxious-face-with-sweat-36.png')
        photo = ImageTk.PhotoImage(self.stresstestImage)
        self.stresstest = Label(self.sidebar, image=photo, bg='#ffffff')
        self.stresstest.image = photo
        self.stresstest.grid(row=1, column=0, pady=(10, 0), padx=(35, 0), sticky="w")

        self.stresstest_text = Button(self.sidebar, text='Stress Test', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff', command=self.show_stresstest)
        self.stresstest_text.grid(row=1, column=1, pady=(10, 0), padx=(0, 25), sticky="w")

        # Mood Tracker
        self.moodtrackerImage = Image.open('assets/dashboard/icons/icons8-slightly-smiling-face-36.png')
        photo = ImageTk.PhotoImage(self.moodtrackerImage)
        self.moodtracker = Label(self.sidebar, image=photo, bg='#ffffff')
        self.moodtracker.image = photo
        self.moodtracker.grid(row=2, column=0, pady=(10, 0), padx=(35, 0), sticky="w")

        self.moodtracker_text = Button(self.sidebar, text='Mood Tracker', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                        cursor='hand2', activebackground='#ffffff', command=self.show_moodtracker)
        self.moodtracker_text.grid(row=2, column=1, pady=(10, 0), padx=(0, 25), sticky="w")

        # Exercise
        self.exerciseImage = Image.open('assets/dashboard/icons/icons8-woman-in-lotus-position-36.png')
        photo = ImageTk.PhotoImage(self.exerciseImage)
        self.exercise = Label(self.sidebar, image=photo, bg='#ffffff')
        self.exercise.image = photo
        self.exercise.grid(row=3, column=0, pady=(10, 0), padx=(35, 0), sticky="w")

        self.exercise_text = Button(self.sidebar, text='Exercise', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                        cursor='hand2', activebackground='#ffffff', command=self.show_exercise)
        self.exercise_text.grid(row=3, column=1, pady=(10, 0), padx=(0, 25), sticky="w")

        # Articles
        self.articlesImage = Image.open('assets/dashboard/icons/icons8-newspaper-emoji-36.png')
        photo = ImageTk.PhotoImage(self.articlesImage)
        self.articles = Label(self.sidebar, image=photo, bg='#ffffff')
        self.articles.image = photo
        self.articles.grid(row=4, column=0, pady=(10, 0), padx=(35, 0), sticky="w")

        self.articles_text = Button(self.sidebar, text='Articles', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff', command=self.show_articles)
        self.articles_text.grid(row=4, column=1, pady=(10, 0), padx=(0, 25), sticky="w")

        # ChatBot
        self.chatbotImage = Image.open('assets/dashboard/icons/icons8-speech-balloon-36.png')
        photo = ImageTk.PhotoImage(self.chatbotImage)
        self.chatbot = Label(self.sidebar, image=photo, bg='#ffffff')
        self.chatbot.image = photo
        self.chatbot.grid(row=5, column=0, pady=(10, 0), padx=(35, 0), sticky="w")

        self.chatbot_text = Button(self.sidebar, text='ChatBot', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff', command=self.show_chatbot)
        self.chatbot_text.grid(row=5, column=1, pady=(10, 0), padx=(0, 25), sticky="w")

        # Exit
        self.exitImage = Image.open('assets/dashboard/icons/icons8-cross-36.png')
        photo = ImageTk.PhotoImage(self.exitImage)
        self.exit = Label(self.sidebar, image=photo, bg='#ffffff')
        self.exit.image = photo
        self.exit.grid(row=6, column=0, pady=(10, 0), padx=(35, 0), sticky="w")

        self.exit_text = Button(self.sidebar, text='Exit', bg='#ffffff', font=("", 13, "bold"), bd=0,
                                cursor='hand2', activebackground='#ffffff', command=self.Exit)
        self.exit_text.grid(row=6, column=1, pady=(10, 0), padx=(0, 25), sticky="w")




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

    def show_chatbot(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
            self.headerText.config(text="ChatBot")
        self.current_frame = self.create_chatbot_frame()
    
    def show_moodtracker(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
            self.headerText.config(text="Mood Tracker")
        self.current_frame = self.create_moodtracker_frame()

    def show_exercise(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
            self.headerText.config(text="Exercise")
        self.current_frame = self.create_exercise_frame()
    
    def show_articles(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
            self.headerText.config(text="Articles")
        self.current_frame = self.create_articles_frame()

    def create_dashboard_frame(self):
        frame = Frame(self.body, bg='#eff5f6')
        frame.place(x=0, y=0, width=1040, height=655)
        frame = DashboardUI(frame, self.username)
        return frame

    def create_stresstest_frame(self):
        frame = Frame(self.body, bg='#eff5f6')
        frame.place(x=0, y=0, width=1040, height=655)
        frame = StressTest(frame, self.username)

        return frame
    
    def create_articles_frame(self):
        frame = Frame(self.body, bg='#eff5f6')
        frame.place(x=0, y=0, width=1066, height=708)
        frame = BlogPage(frame)

        return frame

    def create_exercise_frame(self):
        frame = Frame(self.body, bg='#eff5f6')
        frame.place(x=0, y=0, width=1066, height=708)
        frame = Exercise(frame, self.displayname)
        return frame

    def create_moodtracker_frame(self):
        frame = Frame(self.body, bg='#eff5f6')
        frame.place(x=0, y=0, width=1040, height=655)
        frame = MoodTracker(frame, self.username)

        return frame

    def create_chatbot_frame(self):
        frame = Frame(self.body, bg='#eff5f6')
        frame.place(x=0, y=0, width=1040, height=700)
        frame = ChatUI(frame, self.displayname)

        return frame
    
    def Logout(self):
        if messagebox.askyesno("Logout", " Do you want to logout?") == True:
            self.window.destroy()
            subprocess.run(["python", "login.py"])

    def Exit(self):
        if messagebox.askyesno("Quit", " Leave App?") == True:
            self.window.quit()
            exit(0)

    def win():
        window = Tk()
        Dashboard(window)
        window.mainloop()

if __name__ == '__main__':
    Dashboard.win()
