import tkinter as tk    # üzenetek
import re               # regural expression a jelszavakhoz
from tkinter import *
import subprocess       # subprocess ahhoz, hogyátirányítson a regisztrációs albakhoz
import hashlib


#-------------------------------------------------Path----------------------------------------------------------------

checkboxPath = "txt/checkbox.txt"
smtpPath = "txt/smtp.txt"
usersPath = "txt/users.txt"
usersSavePath = "txt/usersSave.txt"
loggedNamePath = "txt/loggedName.txt"

#-------------------------------------------------Bejelentkezés----------------------------------------------------------------


def login(e1, e2, root):
    #print(type(e1)) 
    username = e1.get()
    # loginhoz a titkosított jelszót átalakítja, és összehasonlítja
    password = hashlib.sha256(e2.get().encode("utf-8")).hexdigest()
    # Open the file in read mode
    with open(usersPath, "r+", encoding="utf8") as f:
        # Read the lines of the file
        line = f.readline()
        while line:
            # Split the line into username and password
            u, p = re.findall(r"Username: (\w+) , PW: (\w+)", line)[0]
            # Check if the username and password match
            if u == username and p == password:
                tk.messagebox.showinfo(
                    "Siker!", f"Sikerült belépni!\nÜdvözöllek {username}!")
                createSession(u)
                root.destroy()
                start_loggedIn_script()
                break
            line = f.readline()
        else:
            tk.messagebox.showerror(
                "Hiba!", "Nem sikerült belépni!")
            e1.delete(0, "end")
            e2.delete(0, "end")

#-------------------------------------------------Registration.py elindul gombnyomásra----------------------------------------------------------------

#Ha csillag van, bármennyi paraméter kaphat

def start_other_script(event):
    subprocess.run(["python", "registration.py"])
    

def start_pwChange_script(*event):
    subprocess.run(["python", "pwChange.py"])
    
def start_pwReminder_script(*event):
    subprocess.run(["python", "pwReminder.py"])
    
def start_loggedIn_script():
    subprocess.run(["python", "loggedIn.py"])
    
def createSession(uname):
    with open(loggedNamePath, "w+", encoding="utf-8") as f:
        f.write(uname)
        f.seek(0)
    
#Nem biztos még
""" def start_mainmenu_script(event):
    subprocess.run(["python", "mainmenu.py"]) """
