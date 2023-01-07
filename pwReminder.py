import customtkinter
import tkinter as tk
from tkinter import *
import smtplib
from email.mime.text import MIMEText
import hashlib

#-------------------------------------------------Alap beállítások----------------------------------------------------------------


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.geometry("500x375")
root.title("Elfelejtett jelszó")
root.resizable(False, False)
#Password reveal variable
reveal_state = tk.BooleanVar()
root.iconbitmap(r'images/favicon.ico')

#-------------------------------------------------Function----------------------------------------------------------------

#basic check stuff
def check_entries():
    name = entry1.get()
    email = entry2.get()
    
    with open("smtp.txt", "r") as f:
        hashed_password = f.read().strip()
        

    if not name or not email:
        tk.messagebox.showerror("Hiba!", "Töltsd ki az össze mezőt!")
        return
    
    try:
        with open("users.txt", "r") as f:
            registered_users = f.read()
            if name not in registered_users:
                tk.messagebox.showerror(
                    "Hiba!", "Nem szerepel a nyilvántartásban ez a felhasználónév!")
                return
    except FileNotFoundError:
        pass
        
    valid_endings = ['.com', '.hu', '.net', '.org', '.edu', '.gov', '.inf', '.biz', '@']
    if not (any(ending in email for ending in valid_endings)) or len(email) < 6:
        tk.messagebox.showerror("Hiba!", "Kérlek valós e-mail címet írj be!")
        return
    
    print("minden valid.")
    
#-------------------------------------------------email sending----------------------------------------------------------------
    
    
    smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
    smtp_ssl_port = 465
    username = 'hajasatlasz@gmail.com'
    password = hashed_password
    sender = 'hajasatlasz@gmail.com'
    targets = entry2.get()

    msg = MIMEText('Megérkezett az új jelszavad! Belépésnél meg tudod majd változtatni!')
    msg['Subject'] = 'Jelszó emlékeztető'
    msg['From'] = sender
    msg['To'] = ', '.join(targets)

    try:
        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username, password)
        server.sendmail(sender, targets, msg.as_string())
        server.quit()
        
        tk.messagebox.showinfo(
            "Siker!", "Elküldtök az e-mailt!\nPerceken belül meg fog érkezni!")
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
button = customtkinter.CTkButton(master=frame, text="Kérem az új jelszót!", command= check_entries)
button.pack(pady=18, padx=10)

label = customtkinter.CTkLabel(
    master=frame, text="Az elfelejtett jelszót e-mailben fogjuk elküldeni! \nMiután megérkezett az üzenet, érdemes megváltoztatni \naz első bejelntkezés előtt!")
label.pack(pady=10, padx=10)


root.mainloop()
