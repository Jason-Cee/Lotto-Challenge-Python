# Jason Calvert
# Lottery Numbers Challenge

# IMPORTS
from tkinter import *
from tkinter import messagebox
import rsaidnumber
import datetime
from datetime import *
import re
from playsound import playsound
import random

root = Tk()
root.title("Lotto Verification")  # WINDOW TITLE
root.geometry("1000x600")  # WINDOW SIZE
root.config(bg="#ffbe0b")  # WINDOW COLOR
root.resizable(False, False)  # NON RESIZEABLE

# CURRENT TIME
now = datetime.now()

# SYMBOLS USED IN EMAIL ADDRESS
reverify = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
# LOTTO IMAGE
img = PhotoImage(file="lotto.png")
Label(root, image=img).place(x=410, y=20)  # LOTTO IMAGE PLACEMENT
# NAME AND SURNAME
name = Label(root, text="Name & Surname: ")
name.config(bg="#212529", fg="#ffbe0b", font="50")  # NAME AND SURNAME SIZE AND COLOR
name.place(x=20, y=150)  # NAME AND SURNAME PLACEMENT
# EMAIL ADDRESS
email = Label(root, text="Email Address: ")
email.config(bg="#212529", fg="#ffbe0b", font="50")  # EMAIL ADDRESS SIZE AND COLOR
email.place(x=600, y=150)  # EMAIL ADDRESS PLACEMENT
# ID NUMBER
idnum = Label(root, text="ID Number: ")
idnum.config(bg="#212529", fg="#ffbe0b", font="50")  # ID NUMBER SIZE AND COLOR
idnum.place(x=330, y=200)  # ID NUMBER PLACEMENT

# NAME AND SURNAME ENTRY
entry1 = Entry(root)
entry1.place(x=750, y=150)
entry1.config(bg="#212529", fg="#ffbe0b", font="50")
# EMAIL ADDRESS ENTRY
entry2 = Entry(root)
entry2.config(bg="#212529", fg="#ffbe0b", font="50")
entry2.place(x=200, y=150)
# ID NUMBER ENTRY
entry3 = Entry(root)
entry3.config(bg="#212529", fg="#ffbe0b", font="50")
entry3.place(x=450, y=200)


# DEFINING LOG IN FUNCTION
def verify():
    # appending text
    w = open("track.txt", "a+")
    w.write("Name: " +
            entry2.get() + " " + "Email Address:" + " " + entry1.get() + " " + "ID Number:" + " " + entry3.get() + " " + "Logged in "
                                                                                                                         "to play "
                                                                                                                         "Lotto at:"
            + str(now) +
            "\n")
    w.close()
    try:
        id_number = rsaidnumber.parse(entry3.get())
        age = str((datetime.today() - id_number.date_of_birth) // timedelta(days=365.25))
        if int(age) >= 18:
            messagebox.showinfo("Success", "Let's Play")
            playsound("DrumrollSound Effect.mp3")
            root.destroy()
            import lotto
        else:
            messagebox.showinfo("INVALID", "You Have To Be Over 18 to Play")
    except ValueError:
        playsound("alert.mp3")
        messagebox.showinfo("INVALID", "Please Enter A Valid 13 Digit ID Number")

    mail = entry2.get()
    if re.search(reverify, mail):
        messagebox.showinfo("SUCCESS", "Valid Email")
    else:
        messagebox.showinfo("INVALID", "Invalid Email")


# DEFINING CLEAR BUTTON FUNCTION
def delete():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')


# DEFINING EXIT BUTTON FUNCTION
def out():
    msg = messagebox.askquestion("Gone So Soon ? ", "Are You Sure You Would Like To Exit ?")  # MESSAGE DISPLAYED
    # WHEN CLICKING EXIT BUTTON
    if msg == "yes":  # IF OPTION IS YES THE WINDOW CLOSES, IF NOT WINDOW STAYS OPEN
        root.destroy()  # CLOSE CURRENT WINDOW


# LOG IN BUTTON
verify_btn = Button(root, width=10, bg="#212529", fg="#f0e68c", font="50", text="Log In", command=verify)
verify_btn.place(x=70, y=550)  # LOG IN BUTTON PLACEMENT

# CLEAR BUTTON
clear_btn = Button(root, width=10, bg="#212529", fg="#f0e68c", font="50", text="Clear", command=delete)
clear_btn.place(x=445, y=550)  # CLEAR BUTTON PLACEMENT

# EXIT BUTTON
exit_btn = Button(root, width=10, bg="#212529", fg="#f0e68c", font="50", text="Exit", command=out)
exit_btn.place(x=800, y=550)  # EXIT BUTTON PLACEMENT

root.mainloop()
