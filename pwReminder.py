import customtkinter
import tkinter as tk
from tkinter import *
import smtplib
from email.mime.text import MIMEText
import re

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
        with open(usersPath, "r+", encoding="utf8") as f:
            line = f.readline()
            while line:
                u, p = re.findall(r"Username: (\w+) , PW: (\w+)", line)[0]
                if u == name and p:
                    send()
                line = f.readline()
            else:
                tk.messagebox.showerror(
                    "Hiba!", "Nem szerepel nyilvántartásban ez a felhasználónév!")
    except FileNotFoundError:
        pass
#-------------------------------------------------email sending----------------------------------------------------------------
def send():
    with open(smtpPath, "r") as f:
        hashed_password = f.read().strip()
        
    smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
    smtp_ssl_port = 465
    username = 'hajasatlasz@gmail.com'
    password = hashed_password
    sender = 'hajasatlasz@gmail.com'
    targets = entry2.get()

    msg = MIMEText(
        f'Kedves {name}!\nMegérkezett az új jelszavad!\n\nBelépésnél meg tudod majd változtatni!\nÜdvözlettel, \n\tHajas Attila István')
    msg['Subject'] = 'Jelszó emlékeztető'
    msg['From'] = sender
    msg['To'] = "".join(targets)

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
