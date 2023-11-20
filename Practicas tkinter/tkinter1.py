import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

label = tk.Label(
    text = "Hello, Tkinter", 
    fg = "black", 
    bg = "#e7e2ce",
    width = 25,
    height = 10
)
label.pack()

button = tk.Button(
    text="Click me!",
    fg = "black",
    bg = "lightblue",
    width = 25,
    height = 5 
)
button.pack()

name = tk.Label(
    text = "Name"
)
name.pack()

entry = tk.Entry()
entry.pack()

window.mainloop()