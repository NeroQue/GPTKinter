from tkinter import *
import customtkinter
import openai
import os
import pickle

# Initiate the app
root = customtkinter.CTk()
root.title("ChatGPT Bot")
root.geometry("1000x600")
root.iconbitmap("logo.ico")


# Set Colored Theme
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")




root.mainloop()