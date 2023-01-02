import customtkinter
import tkinter as tk
import os
import hashlib


#-------------------------------------------------Baisc settings----------------------------------------------------------------


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.geometry("500x350")
root.title("Password change")
root.resizable(False, False)

#-------------------------------------------------functions----------------------------------------------------------------


def pwChange(*event):
    # Get the user input
    username = entry1.get()
    oldPassword = entry2.get()
    newPassword = entry3.get()
    newPasswordagain = entry4.get()
    
    if newPassword != newPasswordagain:
        tk.messagebox.showerror(
            "Hiba!", "Nem egyeznek a jelszavak!")
        return
    
    if not username or not oldPassword or not newPasswordagain or not newPasswordagain:
        tk.messagebox.showerror(
            "Hiba!", "Ne hagyj üresen mezőt!!")
        return
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


root.mainloop()
