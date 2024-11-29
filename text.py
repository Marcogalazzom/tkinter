import tkinter as tk
from tkinter import ttk


# variables
dico = {}
current_word = ""

# function
def word(event):
    global current_word
    char = event.char
    
    if char.isalnum():
        current_word += char
    elif char == " " or char == "\n": 
        if current_word:
            if current_word in dico:
                dico[current_word] += 1
            else:
                dico[current_word] = 1
            print(dico)
            current_word = ""


# window
window = tk.Tk()
window.title("Texte")
window.geometry("1x1")

# widgets
text = tk.Text(window)
text.pack()

# event
window.bind('<KeyPress>', word)

# run
window.mainloop()