import tkinter as tk


def on_click(event):
    print("Label clicked")


root = tk.Tk()
label = tk.Label(root, text="Click me", cursor="hand2")
label.pack()
label.bind("<Button-1>", on_click)
root.mainloop()
