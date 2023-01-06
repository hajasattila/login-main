import customtkinter
import tkinter as tk
from tkinter import *

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


def check_entries():
    name = entry1.get()
    email = entry2.get()

    if not name or not email:
        tk.messagebox.showerror("Hiba!", "Töltsd ki az össze mezőt!")
        return
    print("All the entries are filled out.")
    
    
#-------------------------------------------------PW megmutatása----------------------------------------------------------------





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

label = customtkinter.CTkLabel(
    master=frame, text="Az elfelejtett jelszót e-mailben fogjuk elküldeni! \nMiután megérkezett az üzenet, érdemes megváltoztatni \naz első bejelntkezés előtt!")
label.pack(pady=10, padx=10)


root.mainloop()
