import subprocess
from ttkbootstrap import *
from tkinter import messagebox
from splash import Splash

# MAIN WINDOW
class Main():
    def __init__(self):
        self.show_splash()
        self.run_login()

    def show_splash(self):
        Splash()

    def run_login(self):
        subprocess.run(["python", "login.py"])

if __name__ == "__main__":
    main_window = Main()