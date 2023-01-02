import customtkinter
import tkinter as tk
import os
import hashlib

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.geometry("500x350")
root.title("Password change")
root.resizable(False, False)


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

button = customtkinter.CTkButton(master=frame, text="Megerősítés!")
button.pack(pady=5, padx=100)
button.bind("<Button-1>")


root.mainloop()
