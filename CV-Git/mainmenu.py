import customtkinter  # modern GUI
import tkinter as tk  # üzenetek
import subprocess  # subprocess ahhoz, hogyátirányítson a regisztrációs albakhoz
import re  # regural expression a jelszavakhoz
from tkinter import *


#-------------------------------------------------Kinézet----------------------------------------------------------------


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
root.geometry("500x350")
root.title("Bejelentkezés")
# Set the icon
root.resizable(False, False)
checkbox_var = tk.BooleanVar()


#-------------------------------------------------Functions----------------------------------------------------------------


def login():
    username = entry1.get()
    password = entry2.get()
    # Open the file in read mode
    with open("users.txt", "r+", encoding="utf8") as f:
        # Read the lines of the file
        line = f.readline()
        while line:
            # Split the line into username and password
            u, p = re.findall(r"Username: (\w+) , PW: (\w+)", line)[0]
            # Check if the username and password match
            if u == username and p == password:
                tk.messagebox.showinfo(
                    "Siker!", "Sikerült belépni!")
                entry1.delete(0, "end")
                entry2.delete(0, "end")
                break
            line = f.readline()
        else:
            tk.messagebox.showerror(
                "Hiba!", "Nem sikerült belépni!")
            entry1.delete(0, "end")
            entry2.delete(0, "end")


def start_other_script():
    subprocess.run(["python", "registration.py"])


def save_state():
    username = entry1.get()
    password = entry2.get()
    if len(username) >= 5 and len(password) >= 5:
        with open("checkbox.txt", "w+", encoding="utf8") as f:
            f.write("1" if checkbox_var.get() else "0")
            # Save the username and password in the file
    try:
        with open("usersSave.txt", "w+", encoding="utf8") as f:
            f.write(f"Username: {username} , PW: {password}\n")
            # Read the lines of the file
            line = f.readline()
            while line:
                # Split the line into username and password
                u, p = re.findall(r"Username: (\w+) , PW: (\w+)", line)[0]
                # Check if the username and password already exist in the file
                if u == username and p == password:
                    # Do not write to the file if the username and password already exist
                    break
                line = f.readline()
            else:
                # Write the username and password to the file if they do not already exist
                with open("usersSave.txt", "a", encoding="utf8") as f:
                    f.write(f"Username: {username} , PW: {password}\n")
    except FileNotFoundError:
        pass

def load_state():
    try:
        with open("checkbox.txt", "r+", encoding="utf8") as f:
            state = f.read()
            if state == "1":
                checkbox_var.set(True)
            else:
                checkbox_var.set(False)
    except FileNotFoundError:
        pass

load_state()


#-------------------------------------------------Kinézet----------------------------------------------------------------


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)


label = customtkinter.CTkLabel(master=frame, text="Belépés")
label.pack(pady=12, padx=10)


entry1 = customtkinter.CTkEntry(
    master=frame, placeholder_text="Felhasználónév")
entry1.pack(pady=12, padx=10)


entry2 = customtkinter.CTkEntry(
    master=frame, placeholder_text="Jelszó", show="*")
entry2.pack(pady=12, padx=10)


button = customtkinter.CTkButton(
    master=frame, text="Bejelentkezés", command=login)
button.pack(pady=5, padx=100)
button.bind("<Button>", login)


customtkinter.set_default_color_theme("blue")
button1 = customtkinter.CTkButton(
    master=frame, text="Regisztráció", command=start_other_script)
button1.pack(pady=5, padx=100)
button1.bind("<Button-1>", start_other_script)
# Bind the label to the callback function


customtkinter.set_default_color_theme("green")
checkbox = customtkinter.CTkCheckBox(
    master=frame, text="Emlékezz rám", variable=checkbox_var, command=save_state)
# Disable the checkbox
checkbox.pack(pady=12, padx=10)


def load_u_p():
    try:
        with open("usersSave.txt", "r+", encoding="utf8") as f:
            # Split the line into username and password
            line = f.readline()
            if checkbox_var.get():
                try:
                    u, p = re.findall(r"Username: (\w+) , PW: (\w+)", line)[0]
                    entry1.insert(0, u)
                    entry2.insert(0, p)
                    line = f.readline()
                except Exception:
                    checkbox_var.set(False)
    except FileNotFoundError:
        pass


load_u_p()

root.mainloop()