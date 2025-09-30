import tkinter as tk
from tkinter import ttk

def get_spinboxchange():
  string_var.set( str(double_var.get()) )

# This section creates the Tkinter Window and adds the required elements to it 
window = tk.Tk()
window. title('Tkinter Spinbox Widget')
window.geometry('400x400')

# This is our Spinbox
double_var = tk.DoubleVar()
number_Spinbox = ttk.Spinbox ( from_=0, to=100, increment=.01, textvariable = double_var, font = 'Calibri 24 bold', command= get_spinboxchange)

# Create label
string_var = tk.StringVar()
output_label = ttk.Label(
    window,
    text='',
    font=('Garamond', 20, 'bold'),
    textvariable = string_var,
    foreground='pink',
    justify='center'
)

# Pack elements in frames ready to push onto form/window
number_Spinbox.pack()
output_label.pack()

# run the program to generate window with all placked elements for user interaction
window.mainloop()


