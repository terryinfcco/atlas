import tkinter as tk
from tkinter import ttk


def button_func():
    print("button pressed")


def hello_button():
    print("hello")


# create a window object
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x500")

# ttk label
label = ttk.Label(master=window, text="This is a test")
label.pack()

# tk text
text = tk.Text(master=window)
text.pack()

# ttk label for assignment
my_label = ttk.Label(master=window, text="My Label")
my_label.pack()

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# ttk button
button = ttk.Button(master=window, text="A button", command=button_func)
button.pack()

exercise_button = ttk.Button(master=window, text="exercise", command=hello_button)
exercise_button.pack()


# run - updates the gui, and checks for events
# Loops until the window is closed
window.mainloop()
