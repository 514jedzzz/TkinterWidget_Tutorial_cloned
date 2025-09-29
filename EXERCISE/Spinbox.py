import tkinter as tk
from tkinter import ttk

# This section creates the Tkinter Window and adds the required elements to it 
window = tk.Tk()
window. title('Tkinter Spinbox Widget')
Window.geometry('400x400')

# This is our Spinbox
int_var = tk.IntVar()
Number_Spinbox(window, from_=0, to=100, increment=.01, textvariable = int_var, font = 'Calibri 24 bold')

# Pack elements in frames ready to push onto form/window
Number_spinbox.pack()

# run the program to generate window with all placked elements for user interaction
window.mainloop()

