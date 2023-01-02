import customtkinter
import tkinter as tk
import os
import hashlib

#-------------------------------------------------Alap beállítások----------------------------------------------------------------


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.geometry("500x350")
root.title("Regisztráció")
root.resizable(False, False)
#Password reveal variable
reveal_state = tk.BooleanVar()
root.iconbitmap(r'images/favicon.ico')

#-------------------------------------------------Function----------------------------------------------------------------


def register():
    # Get the user input
    username = entry1.get()
    password = entry2.get()
    passwordagain = entry3.get()

    if not os.path.exists("users.txt"):
        # Create the file
        with open("users.txt", "x", encoding="utf-8") as f:
            pass
    # Validate the input
    if not username or not password:
        tk.messagebox.showerror(
            "Hiba!", "Adj meg egy felhasználónevet, vagy jelszót!")
        return

    if len(username) < 5 or len(password) < 5:
        tk.messagebox.showerror(
            "Figyelmeztetés!", "Túl rövid felhasználónév vagy jelszó!")
        return

    if not any(c.isalpha() for c in username):
        tk.messagebox.showerror(
            "Figyelmeztetés!", "Nem szerepel karakter a felhasználónévben!")
        return

    if password != passwordagain:
        tk.messagebox.showerror(
            "Hiba!", "Nem egyeznek a jelszavak!")
        return

    # Check if the username is already taken
    with open("users.txt", "r+", encoding="utf-8") as f:
        number = 1
        for line in f:
            number += 1
            if username in line:
                tk.messagebox.showerror(
                    "Hiba!", "Ez a felhasználónév, már foglalt!")
                return
    # If the input is valid, write the user data to the file
    # titkosítás a jelszóhoz.
    password = hashlib.sha256(password.encode("utf-8")).hexdigest()
    with open("users.txt", "a+", encoding="utf-8") as f:
        f.write(f"{number}. Username: {username} , PW: {password}\n")

    # Clear the entry fields and show a success message
    # Split the line into parts
    entry1.delete(0, "end")
    entry2.delete(0, "end")
    entry3.delete(0, "end")
    tk.messagebox.showinfo("Siker!", "Sikeres regisztráció!")
    root.destroy()


#-------------------------------------------------PW megmutatása----------------------------------------------------------------

    
def reveal_password():
    if reveal_state.get():
        # Update the show option to reveal the password
        entry2.configure(show="")
        entry3.configure(show="")
    else:
        # Update the show option to hide the password
        entry2.configure(show="*")
        entry3.configure(show="*")

#-------------------------------------------------Frontend----------------------------------------------------------------


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Regisztráció")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Felhasználónév")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Jelszó", show="*")
entry2.pack(pady=12, padx=10)

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Jelszó mégegyszer", show="*")
entry3.pack(pady=12, padx=10)

customtkinter.set_default_color_theme("green")
reveal = customtkinter.CTkCheckBox(master=frame, text="Mutasd a jelszót!", variable=reveal_state, command=reveal_password)
reveal.pack(pady=5, padx=10)

customtkinter.set_default_color_theme("blue")
button = customtkinter.CTkButton(master=frame, text="Regisztrálok!", command=register)
button.pack(pady=5, padx=100)
button.bind("<Button-1>", register)


root.mainloop()
