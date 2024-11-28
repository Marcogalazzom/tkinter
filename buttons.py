import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title("buttons")
window.geometry('600x400')

# button
def button_func():
    print('a basic button')
    print(radio_var.get())

button_string = tk.StringVar(value = "A button with string var")
button = ttk.Button(
    window, 
    text = "A simple button", 
    command = button_func, 
    textvariable= button_string)
button.pack()

# checkbutton
check_var = tk.IntVar(value = 10) # we can also use StringVar, BooleanVar
check1 = ttk.Checkbutton(
    window,
    text="checkbox 1",
    command= lambda: print(check_var.get()),
    variable = check_var,
    onvalue = 10,
    offvalue = 5)
check1.pack()

check2 = ttk.Checkbutton(
    window,
    text = 'checkbox 2',
    command = lambda: check_var.set(5))
check2.pack()

# radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window, 
    text = "Radiobutton 1", 
    value = 1,
    variable = radio_var,
    command = lambda: print(radio_var.get()))
radio1.pack()
radio2 = ttk.Radiobutton(
    window, 
    text = "Radiobutton 2", 
    value = 2,
    variable = radio_var,
    command = lambda: print(radio_var.get()))
radio2.pack()

# radiobuttons
def func_radio():
    print(check_var.get())
    check_var.set(False)


radioexo_var = tk.StringVar()

radioexo1 = ttk.Radiobutton(
    window,
    text = "Radio A",
    value = "A",
    variable= radioexo_var,
    command= func_radio
)
radioexo1.pack()

radioexo2 = ttk.Radiobutton(
    window,
    text = "Radio B",
    value = "B",
    variable = radioexo_var,
    command= func_radio
)
radioexo2.pack()


# another checkbutton
def func_check():
    print(radioexo_var.get())

check_var = tk.BooleanVar()

checkexo = ttk.Checkbutton(
    window,
    text = "exercice check",
    variable = check_var,
    command = func_check,
)
checkexo.pack()


# run 
window.mainloop()