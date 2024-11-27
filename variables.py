import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

# window
window = tk.Tk()
window.title('Tkinter Variables')

# tkinter variable
# you can use a start value : tk.StringVar(value = "start value")
string_var = tk.StringVar()
stringTwo_var = tk.StringVar(value = "test")
 
# widgets
label = ttk.Label(master = window, text = 'label', textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

button = ttk.Button(master = window, text = 'button', command = button_func)
button.pack()

labelTwo = ttk.Label(master = window, text = "yes", textvariable = stringTwo_var)
labelTwo.pack()

entry2 = ttk.Entry(master = window, textvariable= stringTwo_var)
entry2.pack()

entry3 = ttk.Entry(master = window, textvariable= stringTwo_var)
entry3.pack()

# run
window.mainloop()