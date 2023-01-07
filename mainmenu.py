import customtkinter    # modern GUI
import tkinter as tk    # üzenetek
import re               # regural expression a jelszavakhoz
from tkinter import *   #vizualutás
from functions import * #functionokat innen hívom meg

#-------------------------------------------------Kinézet----------------------------------------------------------------
checkboxPath = "txt/checkbox.txt"
smtpPath = "txt/smtp.txt"
usersPath = "txt/users.txt"
usersSavePath = "txt/usersSave.txt"


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
root.geometry("500x375")
root.title("Bejelentkezés")
root.resizable(False, False)
root.iconbitmap(r'images/favicon.ico')

#-------------------------------------------------Text változók----------------------------------------------------------------


checkbox_var = tk.BooleanVar()
reveal_state = tk.BooleanVar()
password = tk.StringVar()


#-------------------------------------------------Functions----------------------------------------------------------------


#-------------------------------------------------UN és PW mentés----------------------------------------------------------------

def save_state():
    username = entry1.get()
    password = entry2.get()
    if len(username) >= 5 and len(password) >= 5:
        with open(checkboxPath, "w+", encoding="utf-8") as f:
            f.write("1" if checkbox_var.get() else "0")
            # Save the username and password in the file
    try:
        with open(usersSavePath, "w+", encoding="utf-8") as f:
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
                with open(usersSavePath, "a", encoding="utf-8") as f:
                    f.write(f"Username: {username} , PW: {password}\n")
    except FileNotFoundError:
        pass
    
#-------------------------------------------------PW megmutatása----------------------------------------------------------------


def reveal_password():
    if reveal_state.get():
        # Update the show option to reveal the password
        entry2.configure(show="")
    else:
        # Update the show option to hide the password
        entry2.configure(show="*")

#-------------------------------------------------Checkbox betöltése----------------------------------------------------------------


def load_state():
    try:
        with open(checkboxPath, "r+", encoding="utf-8") as f:
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
label.pack(pady=10, padx=10)
label.configure(font=("Arial", 20))

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Felhasználónév")
entry1.pack(pady=5, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Jelszó", show="*")
entry2.pack(pady=5, padx=10)

reveal = customtkinter.CTkCheckBox(master=frame, text="Mutasd a jelszót!", variable=reveal_state, command=reveal_password)
reveal.pack(pady=5, padx=10)

customtkinter.set_default_color_theme("green")
checkbox = customtkinter.CTkCheckBox(master=frame, text="Emlékezz rám", variable=checkbox_var, command=save_state)
checkbox.pack(pady=5, padx=10)

button = customtkinter.CTkButton(master=frame, text="Bejelentkezés", command=lambda: login(entry1, entry2, root))
button.pack(pady=5, padx=10)
button.bind("<Button>", lambda: login(entry1, entry2))

customtkinter.set_default_color_theme("blue")
button1 = customtkinter.CTkButton(master=frame, text="Regisztráció", cursor="hand2")
button1.pack(pady=5, padx=10)
# Bind the label to the callback function
button1.bind("<Button-1>", start_other_script)


label1 = customtkinter.CTkLabel(master=frame, text="Jelszó megváltoztatása", cursor="hand2")
label1.pack(pady=5, padx=10)
label1.bind("<Button-1>", start_pwChange_script)

label2 = customtkinter.CTkLabel(master=frame, text="Elfelejtett jelszó?", cursor="hand2")
label2.pack(pady=5, padx=10)
label2.bind("<Button-1>", start_pwReminder_script)
label2.configure(font=("Arial", 12))





#-------------------------------------------------HA van elmentve un és pw betölti a futtatás előtt----------------------------------------------------------------


def load_u_p():
    try:
        with open(usersSavePath, "r+", encoding="utf-8") as f:
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

#Láthatatlanná teszi a filekat.
""" os.system("attrib +h .usersSave.txt") """
root.mainloop()
