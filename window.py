import tkinter as tk
from tkinter import ttk

def button_func():
    print("A button was pressed")

def button_hello():
    print("Hello")

# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# ttk widgets
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

# create widgets
text = tk.Text(master = window)
text.pack()

# ttk entry (single line entry widget)
entry = ttk.Entry(master = window)
entry.pack()

# label
my_label = ttk.Label(master = window, text = "My label")
my_label.pack()

# another button
my_button = ttk.Button(master= window, text="YES", command = button_hello)
my_button.pack()

# ttk button
button = ttk.Button(master = window, text = 'A button', command = button_func)
button.pack()

# run
window.mainloop()