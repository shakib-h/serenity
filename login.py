import hashlib
import subprocess
from tkinter import *
from tkinter import messagebox
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime
import helper
from dashboard import Dashboard

class RegistrationForm:

    def __init__(self, parent):
        self.parent = parent
        self.registration_window = Toplevel(parent)
        self.registration_window.title("Register")
        self.registration_window.geometry("400x800")
        self.registration_window.resizable(0, 0)

        self.username = StringVar(value="Choose your username")
        self.password = StringVar(value="Create a password")
        self.name = StringVar(value="Your Name")
        self.age = StringVar(value="Your Age")
        self.email = StringVar(value="Your Email")
        self.phone = StringVar(value="Your Phone")

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.registration_window, text="Username:").pack(pady=5)
        self.username_entry = Entry(self.registration_window, textvariable=self.username)
        self.username_entry.pack(pady=5)
        self.username_entry.bind("<FocusIn>", self.clear_entry)
        self.username_entry.bind("<FocusOut>", self.restore_default)

        ttk.Label(self.registration_window, text="Password:").pack(pady=5)
        Entry(self.registration_window, textvariable=self.password, show='*').pack(pady=5)

        ttk.Label(self.registration_window, text="Name:").pack(pady=5)
        self.name_entry = Entry(self.registration_window, textvariable=self.name)
        self.name_entry.pack(pady=5)
        self.name_entry.bind("<FocusIn>", self.clear_entry)
        self.name_entry.bind("<FocusOut>", self.restore_default)

        ttk.Label(self.registration_window, text="Age:").pack(pady=5)
        self.age_entry = Entry(self.registration_window, textvariable=self.age)
        self.age_entry.pack(pady=5)
        self.age_entry.bind("<FocusIn>", self.clear_entry)
        self.age_entry.bind("<FocusOut>", self.restore_default)

        ttk.Label(self.registration_window, text="Email:").pack(pady=5)
        self.email_entry = Entry(self.registration_window, textvariable=self.email)
        self.email_entry.pack(pady=5)
        self.email_entry.bind("<FocusIn>", self.clear_entry)
        self.email_entry.bind("<FocusOut>", self.restore_default)

        ttk.Label(self.registration_window, text="Phone:").pack(pady=5)
        self.phone_entry = Entry(self.registration_window, textvariable=self.phone)
        self.phone_entry.pack(pady=5)
        self.phone_entry.bind("<FocusIn>", self.clear_entry)
        self.phone_entry.bind("<FocusOut>", self.restore_default)

        ttk.Button(self.registration_window, text="Submit", command=self.register_user).pack(pady=10)

    def clear_entry(self, event):
        if event.widget.get() in ["Choose your username", "Your Name", "Your Age", "Your Email", "Your Phone"]:
            event.widget.delete(0, END)

    def restore_default(self, event):
        if not event.widget.get():
            default_text = {
                self.username_entry: "Choose your username",
                self.name_entry: "Your Name",
                self.age_entry: "Your Age",
                self.email_entry: "Your Email",
                self.phone_entry: "Your Phone"
            }
            event.widget.insert(0, default_text[event.widget])

    def register_user(self):
        username = self.username.get()
        username = username.lower()
        password = self.password.get()
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        name = self.name.get()
        age = self.age.get()
        email = self.email.get()
        phone = self.phone.get()

        if (username == "Choose your username" or password == "Create a password"
                or name == "Your Name" or age == "Your Age" or email == "Your Email" or phone == "Your Phone"):
            messagebox.showerror("Error", "Please fill out all fields")
            return

        base = mysql.connector.connect(**helper.db_config)
        cur = base.cursor()
        
        # Check username existence
        cur.execute("SELECT username FROM users WHERE username = %s", (username,))
        if cur.fetchone():
            messagebox.showerror("Error", "Username already exists")
            return

        # Check email existence
        cur.execute("SELECT email FROM users WHERE email = %s", (email,))
        if cur.fetchone():
            messagebox.showerror("Error", "Email already exists")
            return

        registration_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                     (username, hashed_password, 'USER', name, age, email, phone, registration_time))
        base.commit()
        messagebox.showinfo("Success", "User registered")
        self.registration_window.destroy()



class Login:

    def __init__(self):
        self.loginw = ttk.Window(themename="darkly")
        self.loginw.title("Serenity")
        self.loginw.geometry(helper.geometry)
        self.loginw.resizable(0, 0)
        self.loginw.protocol('WM_DELETE_WINDOW', self.__login_del__)
        self.loginw.config(bg=helper.accentColor)
        
        background_image = Image.open("assets/background_image.jpg")
        self.background_photo = ImageTk.PhotoImage(background_image)

        self.background_canvas = Canvas(self.loginw, width=helper.width, height=helper.height)
        self.background_canvas.create_image(0, 0, image=self.background_photo, anchor="nw")
        self.background_canvas.pack()

        self.logintable()
        self.username = StringVar(value="Username")
        self.password = StringVar(value="Password")
        self.name = StringVar(value="Your Name")
        self.age = StringVar(value="Your Age")
        self.email = StringVar(value="Your Email")
        self.phone = StringVar(value="Your Phone")
        self.obj()

    def __login_del__(self):
        if messagebox.askyesno("Quit", " Leave App?") == True:
            self.loginw.destroy()
            exit(0)

    def logintable(self):
        self.base = mysql.connector.connect(**helper.db_config)
        self.cur = self.base.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users ("
                         "username VARCHAR(20), password VARCHAR(32) NOT NULL, "
                         "account_type VARCHAR(10) NOT NULL, name VARCHAR(50), "
                         "age VARCHAR(5), email VARCHAR(50), phone VARCHAR(15), "
                         "registration_time TIMESTAMP, PRIMARY KEY (username));")

    def obj(self):
        self.loginframe = ttk.Frame(self.background_canvas, height=400, width=300)  # Put the frame on the canvas
        self.loginw.bind('<Return>', self.checkuser)
        self.loginframe.place(x=1000, y=180)
        self.toplabel = Label(self.loginframe, fg="white", bg="#4267b2", anchor="center", text="Login",
                              font="Roboto 22 bold")
        self.toplabel.place(x=75, y=25)
        self.us = Entry(self.loginframe, width=18, textvariable=self.username, font="Roboto 10 ")
        self.us.place(x=30, y=145, height=40)
        self.pa = Entry(self.loginframe, width=18, textvariable=self.password, font="Roboto 10 ", show='*')
        self.pa.place(x=30, y=195, height=40)
        self.us.bind('<Button-1>', self.onclick)
        self.pa.bind('<Button-1>', self.onclick1)
        self.signin = ttk.Button(self.loginframe, width=20, text="Sign in", command=self.checkuser, bootstyle="SUCCESS")
        self.signin.place(x=30, y=280)
        self.register = ttk.Button(self.loginframe, width=20, text="Register", command=self.show_registration_form, bootstyle="INFO")
        self.register.place(x=30, y=325)

    def show_registration_form(self):
        RegistrationForm(self.loginw)

    def checkuser(self, event=0):
        entered_username = self.username.get()
        entered_username = entered_username.lower()
        entered_password = self.password.get()
        hashed_password = hashlib.md5(entered_password.encode()).hexdigest()

        # Use case-insensitive comparison for the username
        self.cur.execute("SELECT * FROM users WHERE UPPER(username) = %s AND password = %s",
                        (entered_username.upper(), hashed_password))
        
        user_data = self.cur.fetchall()
        
        if user_data:
            self.success()
        else:
            self.fail()

    def success(self):
        messagebox.showinfo("Success", "Login successful")
        self.loginw.destroy()
        subprocess.run(["python", "dashboard.py", "--username", self.username.get()])

    def fail(self):
        messagebox.showerror("Error", "The username or password is incorrect")

    def onclick(self, event):
        if (self.username.get() == "Username" or self.username.get() == "Choose your username"):
            self.us.delete(0, "end")

    def onclick1(self, event):
        if (self.password.get() == "Password" or self.password.get() == "Create a password"):
            self.pa.delete(0, "end")
            self.pa.config(show='*')

if __name__ == "__main__":
    login = Login()
    login.loginw.mainloop()
