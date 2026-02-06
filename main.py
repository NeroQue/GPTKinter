import os
from tkinter import *
import customtkinter
import openai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

# Initiate the app
root = customtkinter.CTk()
root.title("ChatGPT Bot")
root.geometry("600x600")
root.iconbitmap("logo.ico")

# Submit Button Function
def speak():
    # Check Text from Entry Box
    if entry_widget.get():
        if api_key:
            client = openai.OpenAI(api_key=api_key)
            response = client.responses.create(
                                                model="gpt-4o",
                                                input=entry_widget.get(),
                                                instructions="You are a helpful assistant. Answer the user's question as detailed as possible.",
                                                )
            text_widget.insert(END, "\n\n" + response.output_text)
        else:
            print("Please add your OpenAI API key in the .env file.")
            return
    else:
        text_widget.insert(END, "\n\nPlease type something in the entry box.")

# Clear Text
def clear():
    # Clear Main Text Box
    text_widget.delete("1.0", END)
    # Clear Entry Box
    entry_widget.delete(0, END)
    # Lose focus
    root.focus_set()

# Set Colored Theme
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

# Add Text Frame
text_frame = customtkinter.CTkFrame(master=root)
text_frame.pack(pady=10)

# Add Text Widget
text_widget = customtkinter.CTkTextbox(master=text_frame,
                                       bg_color="black",
                                       fg_color="#343638",
                                       border_width=1,
                                       width=500,
                                       )
text_widget.grid(row=0, column=0)

# Entry Widget to type to GPT
entry_widget = customtkinter.CTkEntry(master=root,
                                      placeholder_text="Type here...",
                                      width=500,
                                      height=50,
                                      border_width=1,)
entry_widget.pack(pady=10)

# Create Button Frame
button_frame = customtkinter.CTkFrame(master=root)
button_frame.pack(pady=10)

# Create Buttons
# Submit Button
submit_button = customtkinter.CTkButton(master=button_frame,
                                        text="Submit",
                                        command=speak,
                                        width=200,)
submit_button.grid(row=0, column=0, padx=(0, 5))
# Clear Button
clear_button = customtkinter.CTkButton(master=button_frame,
                                       text="Clear",
                                       command=clear,
                                       width=200,)
clear_button.grid(row=0, column=1, padx=(5, 0))


root.mainloop()