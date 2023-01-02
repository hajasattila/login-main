import tkinter as tk    # üzenetek
import re               # regural expression a jelszavakhoz
from tkinter import *
import subprocess       # subprocess ahhoz, hogyátirányítson a regisztrációs albakhoz
import hashlib

#-------------------------------------------------Bejelentkezés----------------------------------------------------------------

def login(e1, e2):
    print(type(e1))

    username = e1.get()
    # loginhoz a titkosított jelszót átalakítja, és összehasonlítja
    password = hashlib.sha256(e2.get().encode("utf-8")).hexdigest()
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
                e1.delete(0, "end")
                e2.delete(0, "end")
                break
            line = f.readline()
        else:
            tk.messagebox.showerror(
                "Hiba!", "Nem sikerült belépni!")
            e1.delete(0, "end")
            e2.delete(0, "end")

#-------------------------------------------------Registration.py elindul gombnyomásra----------------------------------------------------------------

#Ha csillag van, bármennyi paraméter kaphat

def start_other_script(*event):
    subprocess.run(["python", "registration.py"])
    

def start_pwChange_script(*event):
    subprocess.run(["python", "pwChange.py"])
    
#Nem biztos még
""" def start_mainmenu_script(event):
    subprocess.run(["python", "mainmenu.py"]) """
