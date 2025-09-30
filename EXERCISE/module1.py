import tkinter as tk 
from tkinter import ttk 

# This section creates the Tkinter Window and adds the required 
window = tk.Tk()
window.title('Tkinter Checkbutton Widget')
window.geometry('400x400')

# This is our Checkbutton
bool_var = tk.BooleanVar()
Boolean_checkbutton = ttk.Checkbutton(window, variable = bool_var, text = 'Are uou happy', onvalue = True)

# Pack elements in frames ready to push onto form/window
Boolean_checkbutton.pack()

# run the program to generate window with all packed elements for user interaction
window.mainloop()
