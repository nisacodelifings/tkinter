import tkinter as tk

r = tk.Tk()
r.title('haiii')
button = tk.Button(r, text='stop', width=5, command=r.destroy)
button.pack()
r.mainloop()

"""import tkinter as tk | var = tk.Tk()
from tkinter import * Tk() | var = Tk()""" 