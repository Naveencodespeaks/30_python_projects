import tkinter as tk

root = tk.Tk()
root.mainloop()

label = tk.Label(root, text = "Hello word")
label.pack()

button = tk.Button(root, text  = "click me", command = button_click)
button.pack()

root.mainloop()
