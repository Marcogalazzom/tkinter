import tkinter as tk
from tkinter import ttk
import ttkbootstrap

def convert():
	try:	
		mile_input = float(entry_float.get())
		km_output = round(mile_input * 1.61, 2)
		string = f"{km_output} kilometers"
		output_string.set(string)
	except:
		output_string.set("INPUT A NUMBER")

# window
window = tk.Tk()					
window.title('Converter')
window.geometry('300x150')

# title
title_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Calibri 24 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry_float = tk.DoubleVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_float) 
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 5)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
	master = window,
	 text = 'Output',
	 font = 'Calibri 24',
	 textvariable = output_string)
output_label.pack()

# run
window.mainloop()
