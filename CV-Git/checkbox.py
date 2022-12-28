import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Checkbox Example")

# Function to save the checkbox state to a file


def save_state():
    with open("checkbox.txt", "w") as f:
        f.write("1" if checkbox_var.get() else "0")

# Function to load the checkbox state from a file


def load_state():
    try:
        with open("checkbox.txt", "r") as f:
            state = f.read()
            if state == "1":
                checkbox_var.set(True)
            else:
                checkbox_var.set(False)
    except FileNotFoundError:
        pass


# Create a checkbox variable
checkbox_var = tk.BooleanVar()

# Create the checkbox and a button
checkbox = tk.Checkbutton(text="Remember me", variable=checkbox_var)
checkbox.pack()

button = tk.Button(text="Save", command=save_state)
button.pack()

# Load the checkbox state when the program starts
load_state()

# Run the main loop
window.mainloop()
