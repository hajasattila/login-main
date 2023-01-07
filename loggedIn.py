import customtkinter
import tkinter as tk
from functions import *
import os
""" from mainmenu import root as r """


#-------------------------------------------------Baisc settings----------------------------------------------------------------

checkboxPath = "txt/checkbox.txt"
smtpPath = "txt/smtp.txt"
usersPath = "txt/users.txt"
usersSavePath = "txt/usersSave.txt"
loggedNamePath = "txt/loggedName.txt"

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.geometry("500x375")
root.title("Main program")
root.resizable(False, False)
root.iconbitmap(r'images/favicon.ico')
#-------------------------------------------------functions----------------------------------------------------------------
try:
    with open(loggedNamePath, "r", encoding="utf-8") as f:
        line = f.readline()
except FileExistsError as e:
    pass
    
def exit(event):
    os.remove(loggedNamePath)
    root.destroy()
    subprocess.run(["python", "mainmenu.py"])
    
    
    

#-------------------------------------------------Frontend----------------------------------------------------------------


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text=f"Üdvözlünk {line}")
label.pack(pady=50, padx=10)
label.configure(font=("Arial", 20))

label = customtkinter.CTkLabel(master=frame, text="Kijelentkezés", cursor="hand2")
label.pack(pady=5, padx=10)
label.bind("<Button-1>", exit)
label.configure(font=("Arial", 12))


root.mainloop()
