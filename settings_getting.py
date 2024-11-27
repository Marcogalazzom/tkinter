import tkinter as tk
from tkinter import ttk

def button_func():
    # get the content of the entry
    user_text = entry.get()

    # update the label
    label['text'] = user_text
    
    # desactive the button
    entry['state'] = "disabled" 
    
    # all the options you can use
    # label.configure() 

def reset_func():
    label['text'] = "Some text"
    entry['state'] = "enabled"

# window
window = tk.Tk()
window.title("Getting and setting widgets")
window.geometry("800x800")

# widgets
label = ttk.Label(master = window, text = "Some text")
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = "The button", command = button_func)
button.pack()

reset_button = ttk.Button(master = window, text = "Reset", command = reset_func)
reset_button.pack()

# run
window.mainloop()