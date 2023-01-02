# login

My first own login and registration program. Written in python, with a simple GUI. 

------------------------------------------------------------------------------------------------------------------------


ENG:


Libraries in the program, what I am working with:


    customtkinter -> for the simple, and fast prebuild GUI
        tkinter -> simple messages
    re -> regular expressions
    hashlib -> password security
    os -> for basic Operating System commands


If these are not installed, it's not possible to run the program from the editor.
    Install command:    - pip install "nameOfTheLibrary"


Rules apply to registration:
- The username and password must be at least 5 characters long. 
- All fields must be filled in, nothing can be left blank.
- The username must contain at least one letter.
- Passwords must match.
- You cannot save data with the check mark, if the username or password is missing.
- The password can be changed, if you click "jelszó megváltoztatása" label.
- If you want to change your password, the same rules apply as for registration.


If something was wrong with the process, the program will send a warning or an error message.


If everything was alright, the registration and login will be successful!


------------------------------------------------------------------------------------------------------------------------


HU:


A programban szereplő könyvtárak, amikkel dolgozom: 

    customtkinter -> előre létrehozott gyors GUI
        tkinter -> egyszerű üzenetek
    re -> reguláris kifejezések
    hashlib -> jelszó biztonság
    os -> Operációs rendszer parancsok

Ha ezek nincsenek telepítve, a program nem futtatható a szerkesztőből.
    Telepítési parancs:     - pip install "konyvtarNeve"


Szabályok vonatkoznak a regisztrációhoz:
- Minimum 5 karakter hosszúnak kell lennie a felhasználónévnek és a jelszónak is. 
- Minden mezőt ki kell tölteni, nem lehet üresen hagyni semmit.
- A felhasználónévnek muszáj tartalmazzon legalább egy betűt.
- A jelszavaknak meg kell egyezzenek.
- Nem lehet elmenteni úgy adatot az "Emlékezz rám" gombbal, hogy csak felhasználónév, vagy jelszó van megadva.
- A jelszó megváltoztatható, ha rákattintunk a "jelszó megváltoztatása" feliratra.
- Ha szeretnéd megváltoztatni jelszavad, ugyanazok a szabályok érvényesek, mint a regisztrációnál.


Ha valami hibás, akkor figyelmeztetést, vagy hiba üzenetet fog a program küldeni.


Ha minden megfelelő, akkor a regisztráció, és a belépés is sikeres lesz!


------------------------------------------------------------------------------------------------------------------------
