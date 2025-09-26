import tkinter as tk
from tkinter import ttk
 
# Function to update the label text
def set_label():
    output_label.config(text=output_label.cget("text") + "_Edited")
 
# Create window
window = tk.Tk()
window.title('Tkinter Label Widget')
window.geometry('400x400')
 
# Create label
output_label = ttk.Label(
    window,
    text='This is my Label',
    font=('Garamond', 20, 'bold'),
    foreground='pink',
    justify='center'
)
output_label.configure(underline=10)  # Underline the 'L' in "Label"
output_label.pack(pady=20)
 
# Button to update label
ttk.Button(window, text='Update Label', command=set_label).pack(pady=10)
 
# Run app
window.mainloop()