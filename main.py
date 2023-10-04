from ttkbootstrap import *
from tkinter import messagebox
from login import Login
from splash import Splash

# MAIN WINDOW


class Main(Login):

    def __init__(self):
        Splash()

    def __init__(self):
        Login.__init__(self)
        self.loginw.mainloop()
        self.loginw.state('withdraw')  # LOGIN WINDOW EXITS
        self.mainw = Toplevel(bg="#FFFFFF")
        width = 1400
        height = 780
        screen_width = self.mainw.winfo_screenwidth()
        screen_height = self.mainw.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.mainw.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.mainw.title("Inventory")
        self.mainw.resizable(0,0)
        self.mainw.protocol('WM_DELETE_WINDOW', self.__Main_del__)
        self.getdetails()



if __name__ == '__main__':
    app = Main()
    app.base.commit()
    app.mainw.mainloop()


