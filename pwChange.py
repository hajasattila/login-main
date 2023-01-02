import customtkinter
import tkinter as tk
import re
import hashlib
from functions import *


#-------------------------------------------------Baisc settings----------------------------------------------------------------


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.geometry("500x375")
root.title("Password change")
root.resizable(False, False)

#-------------------------------------------------functions----------------------------------------------------------------
                
def pwChange(*event):
    # Get the user input
    username = entry1.get()
    oldPassword = entry2.get()
    newPassword = entry3.get()
    newPasswordagain = entry4.get()
    number = 0

    if oldPassword == newPassword:
        tk.messagebox.showerror("Hiba!", "Az új jelszavad nem lehet a régi!")
        return

    if newPassword != newPasswordagain:
        tk.messagebox.showerror("Hiba!", "Nem egyeznek az új jelszavak!")
        return
    
    if not username or not oldPassword or not newPassword or not newPasswordagain:
        tk.messagebox.showerror("Hiba!", "Ne hagyj üresen mezőt!")
        return
    
    if len(newPassword) < 5:
        tk.messagebox.showerror("Figyelmeztetés!", "Vigyázz! \n5 karakternél rövidebb a jelszavad!")
        return

    # Hash the old password for comparison
    hashed_old_password = hashlib.sha256(oldPassword.encode("utf-8")).hexdigest()

    with open("users.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Check if the username and password match
    for i, line in enumerate(lines):
        number += 1
        u, p = re.findall(r"Username: (\w+) , PW: (\w+)", line)[0]
        if u == username and p == hashed_old_password:
            # Hash the new password
            hashed_new_password = hashlib.sha256(newPassword.encode("utf-8")).hexdigest()
            lines[i] = f"{number}. Username: {username} , PW: {hashed_new_password}\n"
            break
    else:
        tk.messagebox.showerror("Hiba!", "Nem sikerült frissíteni a jelszót!")
        return
    
    with open("users.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)
    tk.messagebox.showinfo("Siker!", "Sikeresen frissült a jelszavad!")
    root.destroy()

#-------------------------------------------------Frontend----------------------------------------------------------------


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Jelszó változtatás")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Felhasználónév")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Régi jelszó", show="*")
entry2.pack(pady=12, padx=10)

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Új jelszó", show="*")
entry3.pack(pady=12, padx=10)

entry4 = customtkinter.CTkEntry(master=frame, placeholder_text="Új jelszó mégegyszer", show="*")
entry4.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Megerősítés!", command=lambda: pwChange)
button.pack(pady=5, padx=100)
button.bind("<Button-1>", pwChange)

#Nem biztos még, hogy kelleni fog
""" label1 = customtkinter.CTkLabel(master=frame, text="Mainmenu", cursor="hand2")
label1.pack(pady=5, padx=10)
label1.bind("<Button-1>", start_mainmenu_script) """


root.mainloop()
