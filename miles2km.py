import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk


# Function to run when the button is clicked
def convert():
    # grab what's in the entry widget
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)


# Create main window
window = tk.Tk()
# Put a title on the window
window.title("Demo")
# Set geometry of window - width then height in pixels
window.geometry("300x150")
# Create a title label on the window itself
# Needs the container and some text at a minimum
# Font is optional but commonly used for styling
title_label = ttk.Label(
    master=window, text="Miles to kilometers", font="Calibri 24 bold"
)
# Has to be placed on the window somehow - pack is the simplest
title_label.pack()
# Three different widgets for the input - a container (a frame), an entry widget and a button
input_frame = ttk.Frame(master=window)
# Create a tkinter variable to get the value in the entry field
entry_int = tk.IntVar()
# and connect our tkinter variable to the entry widget using textvariable
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
# Notice no parentheses following command=convert
button = ttk.Button(master=input_frame, text="Convert", command=convert)
# Side left gets the widgets on the same line
# padx puts some space between the entry field and the button
entry.pack(side="left", padx=10)
button.pack(side="left")
# pady puts some space between the title label and the frame for input
input_frame.pack(pady=10)
# last widget is a label to put the output again using tkinter variables
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window, text="Output", font="Calibri 24", textvariable=output_string
)
output_label.pack(pady=5)

# run the app
window.mainloop()
