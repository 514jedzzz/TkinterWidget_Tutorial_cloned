import tkinter as tk
from tkinter import ttk
 
# window
window = tk.Tk()
window.title('Tkinter Combobox Widget')
window.geometry('400x400')
 
# Label to show selected option
label = tk.Label(window, text="Select an option from the combobox")
label.pack(pady=10)
 
# Function to update label based on combobox selection
def on_select(event):
    selected_option = string_var.get()
    label.config(text=f"Selected: {selected_option}")
 
# Function to be called before dropdown list is shown
def update_combobox_values():
    # This function runs before dropdown is displayed.
    # Here you could dynamically update values or do other stuff.
    print("postcommand triggered: Dropdown about to open")
    # For demonstration, let's just update the combobox values dynamically
    # (You can remove or modify this part)
    myCombobox['values'] = ['This Option', 'That Option', 'Another Option', 'New Dynamic Option']
 
# Combobox widget
string_var = tk.StringVar()
myCombobox = ttk.Combobox(
    master=window,
    textvariable=string_var,
    values=['This Options', 'That Options', 'Another Option'],
    postcommand=update_combobox_values  # runs before dropdown opens
)
 
# Bind the selection event to the update function
myCombobox.bind("<<ComboboxSelected>>", on_select)
 
# pack
myCombobox.pack()
 
# run
window.mainloop()