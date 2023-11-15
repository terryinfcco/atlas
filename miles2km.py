import tkinter as tk
from tkinter import ttk

# Create main window
window = tk.Tk()
# Put a title on the window
window.title('Demo')
# Set geometry of window - width then height in pixels
window.geometry('300x150')
# Create a title label on the window itself
# Needs the container and some text at a minimum
# Font is optional but commonly used for styling
title_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'C059 24 bold')
# Has to be placed on the window somehow - pack is the simplest
title_label.pack()
# Three different widgets for the input - a container (a frame), an entry widget and a button
input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame)
button = ttk.Button(master=input_frame, text='Convert')
entry.pack()
button.pack()
input_frame.pack()
# run the app
window.mainloop()