from ttkbootstrap import *
from tkinter import messagebox
from login import Login
from splash import Splash

# MAIN WINDOW
class Main(Login):
    def __init__(self):
        Splash()
        Login.__init__(self)
        self.loginw.mainloop()

if __name__ == '__main__':
    app = Main()
    app.base.commit()
    app.mainw.mainloop()