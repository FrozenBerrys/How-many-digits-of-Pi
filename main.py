#!/usr/bin/env python      
import tkinter as tk, ispi
from tkinter import ttk   

def convert():
    input = entry_int.get()
    output = ispi.ispi(input)
    text = output[0] + output[1]
    output_string.set(text)

window = tk.Tk()
window.title("Typing Speed Tester")  
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f"{400}x{200}")

#title
title_label = ttk.Label(master = window, text = " How many digits of \n π do you remember? ", font = 'Calibri 24 bold')
title_label.pack(pady = 10)

#input field
input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "Check", command = convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'right')
input_frame.pack(pady = 10)

#output label 
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri, 24', textvariable = output_string)
output_label.pack(padx = 5)

window.mainloop()

