import tkinter as tk
from tkinter import ttk

def button_func():
    # get content of entry using get method
    entry_text = test_entry.get()
    # update the label - 2 ways to do it - he prefers the second
    # test_label.config(text = entry_text)
    test_label['text'] = entry_text
    # print(test_entry.configure())

def reset_func():
    test_label['text'] = 'some text'
    test_entry.delete(0, 'end')

# window = tk.Tk()
window = tk.Tk()
window.title('Getting and setting widgets')

# widgets to test with

# label
test_label = ttk.Label(window, text='test label')
test_label.pack()

# entry
test_entry = ttk.Entry(window)
test_entry.pack()

# buttons
test_button = ttk.Button(window, text='click me', command=button_func)
test_button.pack()

reset_button = ttk.Button(window, text='reset entry box', command=reset_func)
reset_button.pack()
# run
window.mainloop()