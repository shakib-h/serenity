from tkinter import *
from tkinter import messagebox
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from PIL import Image, ImageTk  # Import PIL modules
import mysql.connector
import helper
from dashboard import Dashboard

# LOGIN CLASS
class Login:

    def __init__(self):
        self.loginw = ttk.Window(themename="darkly")
        self.loginw.title("Serenity")
        self.loginw.geometry(helper.geometry)
        self.loginw.resizable(0, 0)
        self.loginw.protocol('WM_DELETE_WINDOW', self.__login_del__)
        self.loginw.config(bg=helper.accentColor)
        
        # Load the background image
        background_image = Image.open("assets/background_image.jpg")
        self.background_photo = ImageTk.PhotoImage(background_image)

        # Create a canvas to display the background image
        self.background_canvas = Canvas(self.loginw, width=helper.width, height=helper.height)
        self.background_canvas.create_image(0, 0, image=self.background_photo, anchor="nw")
        self.background_canvas.pack()

        self.logintable()
        self.username = StringVar(value="Username")
        self.password = StringVar(value="Password")
        self.obj()

    def __login_del__(self):
        if messagebox.askyesno("Quit", " Leave App?") == True:
            self.loginw.destroy()
            exit(0)  # FORCE SYSTEM TO EXIT

    # LOGIN TABLE
    def logintable(self):
        self.base = mysql.connector.connect(**helper.db_config)
        self.cur = self.base.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS users (username VARCHAR(20),password VARCHAR(20) NOT NULL,account_type VARCHAR(10) NOT NULL,PRIMARY KEY (username));")

    # WIDGET FUNCTION
    def obj(self):
        self.loginframe = ttk.Frame(self.background_canvas, height=400, width=300)  # Put the frame on the canvas
        self.loginw.bind('<Return>', self.checkuser)
        self.loginframe.place(x=1000, y=180)
        self.toplabel = Label(self.loginframe, fg="white", bg="#4267b2", anchor="center", text="Login",
                              font="Roboto 40 bold")
        self.toplabel.place(x=75, y=25)
        self.us = ttk.Entry(self.loginframe, width=20, textvariable=self.username, font="Roboto 14 ")
        self.us.place(x=35, y=145, height=40)
        self.pa = ttk.Entry(self.loginframe, width=20, textvariable=self.password, font="Roboto 14 ")
        self.pa.place(x=35, y=195, height=40)
        self.us.bind('<Button-1>', self.onclick)
        self.pa.bind('<Button-1>', self.onclick1)
        self.signin = ttk.Button(self.loginframe, width=20, text="Sign in", command=self.checkuser, bootstyle="SUCCESS")
        self.signin.place(x=30, y=280)
        self.register = ttk.Button(self.loginframe, width=20, text="Register", command=self.reguser, bootstyle="INFO")
        self.register.place(x=30, y=325)

    # CHECK USER IN DATABASE
    def checkuser(self, event=0):
        s = self.username.get()
        s1 = self.password.get()
        s = s.upper()
        s1 = s1.upper()
        self.cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (s, s1))
        l = self.cur.fetchall()
        if (len(l) > 0):
            self.success()
        else:
            self.fail()

    # LOGIN SUCCESS
    def success(self):
        messagebox.showinfo("Success","Login successful")
        self.loginw.destroy()

    # LOGIN FAILURE
    def fail(self):
        messagebox.showerror("Error", "The username or password is incorrect")

    # USER REGISTRATION && LOGIN->REGISTER
    def reguser(self):
        self.toplabel.config(text="Register")
        self.toplabel.place(x=40, y=25)
        self.username.set("Choose your username")
        self.password.set("Create a password")
        self.signin.config(text="Ok", command=self.insert)
        self.register.place(x=35, y=335)
        self.register.config(text="Back", command=self.revert)
        self.signin.config()
        self.signin.place(x=35, y=290)
        self.pa.config(show='')
        self.loginw.focus()
        self.loginw.bind('<Return>', self.insert)
        self.loginw.title('Register')

    # REGISTER USER TO DATABASE
    def insert(self, event=0):
        s = self.username.get()
        s1 = self.password.get()
        s = s.upper()
        s1 = s1.upper()
        self.cur.execute("select username from users where username = %s", (s,))
        l = self.cur.fetchall()
        if (len(l) > 0):
            messagebox.showerror("Error", "Username already exists")
            self.username.set('Choose your username')
            self.loginw.focus()
            return
        if (len(s) == 0 or len(s1) == 0 or len(s) > 20 or len(s1) > 20 or s1 == "CREATE A PASSWORD" or s == 'CHOOSE YOUR USERNAME'):
            messagebox.showerror("Error", "Invalid username or password")
            self.username.set('Choose your username')
            self.password.set('Create a password')
            self.pa.config(show='')
            self.loginw.focus()
            return
        else:
            self.cur.execute("insert into users values(%s,%s,%s)", (s, s1, 'USER'))
            messagebox.showinfo("Success", "User registered")
            self.base.commit()
            self.revert()
            # ADD
            self.loginw.state('withdraw')
            self.tree.delete(*self.tree.get_children())
            self.getusers()

    # REGISTER->LOGIN
    def revert(self):
        self.toplabel.config(text="Login")
        self.toplabel.place(x=75, y=25)
        self.username.set("Username")
        self.password.set("Password")
        self.signin.config(text="Login", command=self.checkuser)
        self.register.place(x=35, y=335)
        self.register.config(text="Register", command=self.reguser)
        self.signin.config()
        self.signin.place(x=35, y=290)
        self.pa.config(show='')
        self.loginw.focus()
        self.loginw.bind('<Return>', self.checkuser)
        self.loginw.title('Login')

    # ONCLICK EVENTS
    def onclick(self, event):
        if (self.username.get() == "Username" or self.username.get() == "Choose your username"):
            self.us.delete(0, "end")

    def onclick1(self, event):
        if (self.password.get() == "Password" or self.password.get() == "Create a password"):
            self.pa.delete(0, "end")
            self.pa.config(show="*")

if __name__ == "__main__":
    login = Login()
    login.loginw.mainloop()
