import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading
import requests
from io import BytesIO

class BlogPage:

    def destroy(self):
        self.parent_frame.destroy()