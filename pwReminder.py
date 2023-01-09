import customtkinter
import tkinter as tk
from tkinter import *
import smtplib
from email.mime.text import MIMEText
import re
import string
import random
import hashlib

#-------------------------------------------------PATH----------------------------------------------------------------

checkboxPath = "txt/checkbox.txt"
smtpPath = "txt/smtp.txt"
usersPath = "txt/users.txt"
usersSavePath = "txt/usersSave.txt"
loggedNamePath = "txt/loggedName.txt"

#-------------------------------------------------Alap beállítások----------------------------------------------------------------

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.geometry("500x375")
root.title("Elfelejtett jelszó")
root.resizable(False, False)
root.iconbitmap(r'images/favicon.ico')

#-------------------------------------------------Function----------------------------------------------------------------


def generate_password():
    characters = string.ascii_letters + string.digits
    password_length = random.randint(6, 16)
    password = ''.join(random.choice(characters)for i in range(password_length))
    return password

global newPassword
newPassword = generate_password()

#basic check stuff
def check_entries():
    global name
    name = entry1.get()
    email = entry2.get()
    valid_endings = ['.com', '.hu', '.net', '.org',
                     '.edu', '.gov', '.inf', '.biz', '@']
    
    if not (any(ending in email for ending in valid_endings)) or len(email) < 6:
        tk.messagebox.showerror("Hiba!", "Kérlek valós e-mail címet írj be!")
        return

    if not name or not email:
        tk.messagebox.showerror("Hiba!", "Töltsd ki az össze mezőt!")
        return

    try:
        with open(usersPath, "r+", encoding="utf-8") as f:
            line = f.readline()
            while line:
                u, p = re.findall(r"Username: (\w+) , PW: (\w+)", line)[0]
                if u == name and p:
                    send()
                    break
                line = f.readline()
            else:
                tk.messagebox.showerror("Hiba!", "Nem szerepel nyilvántartásban ez a felhasználónév!")
    except FileNotFoundError:
        pass
    
#-------------------------------------------------pwChange----------------------------------------------------------------

def pwChange(*event):
    with open(usersPath, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        number = 0
        # Check if the username and password match
        for i, line in enumerate(lines):
            number += 1
            u, p = re.findall(r"Username: (\w+) , PW: (\w+)", line)[0]
            if u == name and p:
                # Hash the new password
                hashed_new_password = hashlib.sha256(newPassword.encode("utf-8")).hexdigest()
                lines[i] = f"{number}. Username: {name} , PW: {hashed_new_password}\n"
                break
        else:
            tk.messagebox.showerror("Hiba!", "Nem sikerült frissíteni a jelszót!")
            return
        
        with open(usersPath, "w+", encoding="utf-8") as f:
            f.writelines(lines)
    
#-------------------------------------------------email sending----------------------------------------------------------------
def send():
    
    with open(smtpPath, "r+") as f:
        hashed_password = f.read().strip()
    
    smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
    smtp_ssl_port = 465
    username = 'hajasatlasz@gmail.com'
    password = hashed_password
    sender = 'hajasatlasz@gmail.com'
    targets = entry2.get()

    msg = MIMEText(
        f'Kedves {name}!\nMegérkezett az új jelszavad!\nAz új jelszavad: \t" {newPassword} " \nBelépésnél meg tudod majd változtatni!\nÜdvözlettel, \n\tHajas Attila István')
    msg['Subject'] = 'Jelszó emlékeztető'
    msg['From'] = sender
    msg['To'] = "".join(targets)

    pwChange()
    
    try:
        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username, password)
        server.sendmail(sender, targets, msg.as_string())
        server.quit()

        tk.messagebox.showinfo(
            "Siker!", f"Elküldtök az e-mailt {name}!\nPerceken belül meg fog érkezni!")
        root.destroy()
    except Exception as e:
        tk.messagebox.showerror("Hiba!", e)

#-------------------------------------------------Frontend----------------------------------------------------------------
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Elfelejtett jelszó")
label.pack(pady=12, padx=10)
label.configure(font=("Arial", 20))

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Felhasználónév")
entry1.pack(pady=18, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="E-mail cím")
entry2.pack(pady=18, padx=10)

customtkinter.set_default_color_theme("blue")
button = customtkinter.CTkButton(master=frame, text="Kérem az új jelszót!", command=check_entries)
button.pack(pady=18, padx=10)

label = customtkinter.CTkLabel(master=frame, text="Az elfelejtett jelszót e-mailben fogjuk elküldeni! \nMiután megérkezett az üzenet, érdemes megváltoztatni \naz első bejelntkezés előtt!")
label.pack(pady=10, padx=10)

root.mainloop()
