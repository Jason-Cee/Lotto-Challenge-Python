# Jason Calvert
# Lottery Numbers Challenge

# IMPORTS
from tkinter import *
from tkinter import messagebox
import datetime
from datetime import *
import re
from playsound import playsound
import random
import uuid

root = Tk()
root.title("Lotto Verification")  # WINDOW TITLE
root.geometry("1000x600")  # WINDOW SIZE
root.config(bg="#ffbe0b")  # WINDOW COLOR
root.resizable(False, False)  # NON RESIZEABLE

# CURRENT TIME
now = datetime.now()

# SYMBOLS USED IN EMAIL ADDRESS
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# LOTTO IMAGE
limg = PhotoImage(file="lotto.png")
Label(root, image=limg).place(x=410, y=20)  # LOTTO IMAGE PLACEMENT
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
entry1.place(x=200, y=150)
entry1.config(bg="#212529", fg="#ffbe0b", font="50")
# EMAIL ADDRESS ENTRY
entry2 = Entry(root)
entry2.config(bg="#212529", fg="#ffbe0b", font="50")
entry2.place(x=750, y=150)
# ID NUMBER ENTRY
entry3 = Entry(root)
entry3.config(bg="#212529", fg="#ffbe0b", font="50")
entry3.place(x=450, y=200)

uuid.uuid4()
user_id = uuid.uuid4()


# DEFINING LOG IN FUNCTION


def success():
    # SYMBOLS USED IN EMAIL ADDRESS
    global dob
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if entry1.get() == "":
        messagebox.showerror("INVALID", "PLEASE ENTER NAME AND SURNAME")
    elif len(entry3.get()) > 13 or len(entry3.get()) < 13:
        messagebox.showerror("INVALID", "PLEASE ENTER VALID 13 DIGIT ID NUMBER")
    elif not re.search(regex, entry2.get()):
        messagebox.showerror("INVALID", "PLEASE ENTER VALID EMAIL ADDRESS")
    else:
        root.destroy()
        import lotto

        try:
            id = entry3.get()
            year = id[:2]
            if year >= "22":
                year = "19" + year
            else:
                year = "20" + year
            month = id[2:4]
            day = id[4:6]
            dob = year, month, day
            today = date.today()
            age = today.year - int(year) - ((today.month, today.day) < (int(month), int(day)))
            if age >= 18:
                messagebox.showinfo("SUCCESS", "LET'S PLAY")
                import lotto
            elif age < 18:
                messagebox.showerror("INVALID", "YOU HAVE TO BE 18 OR OLDER TO PLAY")
        except:
            messagebox.showerror("Error", "Something went wrong")
            root.destroy()

    w = open("track.txt", "a+")
    w.write("Name: " +
            entry1.get() + " " + "Email Address:" + " " + entry2.get() + " " + "ID Number:" + " " + entry3.get() + " " +
            "Logged in "
            "to play "
            "Lotto at:"
            + str(now) + "\n" + "User ID Is: " + str(user_id) + " " + dob +
            "\n")
    w.close()


# LOTTO IMAGE
img = PhotoImage(file="flag.png")
Label(root, image=img).place(x=85, y=250)  # LOTTO IMAGE PLACEMENT


# DEFINING CLEAR BUTTON FUNCTION
def delete():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    playsound("ha.mp3")


# DEFINING EXIT BUTTON FUNCTION
def out():
    playsound("alert.mp3")
    msg = messagebox.askquestion("Gone So Soon ? ", "Are You Sure You Would Like To Exit ?")  # MESSAGE DISPLAYED
    # WHEN CLICKING EXIT BUTTON
    if msg == "yes":  # IF OPTION IS YES THE WINDOW CLOSES, IF NOT WINDOW STAYS OPEN
        root.destroy()  # CLOSE CURRENT WINDOW


# LOG IN BUTTON'
verify_btn = Button(root, width=10, bg="#212529", fg="#f0e68c", font="50", text="Log In", command=success)
verify_btn.place(x=70, y=550)  # LOG IN BUTTON PLACEMENT

# CLEAR BUTTON
clear_btn = Button(root, width=10, bg="#212529", fg="#f0e68c", font="50", text="Clear", command=delete)
clear_btn.place(x=445, y=550)  # CLEAR BUTTON PLACEMENT

# EXIT BUTTON
exit_btn = Button(root, width=10, bg="#212529", fg="#f0e68c", font="50", text="Exit", command=out)
exit_btn.place(x=800, y=550)  # EXIT BUTTON PLACEMENT

root.mainloop()
