from tkinter import *
from tkinter import messagebox
from playsound import playsound
import random

root = Tk()
root.title("Lotto Verification")  # WINDOW TITLE
root.geometry("1000x600")  # WINDOW SIZE
root.config(bg="#ffbe0b")  # WINDOW COLOR
root.resizable(False, False)  # NON RESIZEABLE

# LOTTO IMAGE
img = PhotoImage(file="lotto.png")
Label(root, image=img).place(x=410, y=20)  # LOTTO IMAGE PLACEMENT

# LABEL BOX
frame = LabelFrame(root, width=950, height=100, text="Your Numbers", bg="#49af62")
frame.place(x=25, y=150)
# SPIN BOXES
box = Spinbox(frame, from_=1, to=49, width=2, font=("Ariel", 30))
box.place(x=70, y=10)
box2 = Spinbox(frame, from_=1, to=49, width=2, font=("Ariel", 30))
box2.place(x=230, y=10)
box3 = Spinbox(frame, from_=1, to=49, width=2, font=("Ariel", 30))
box3.place(x=370, y=10)
box4 = Spinbox(frame, from_=1, to=49, width=2, font=("Ariel", 30))
box4.place(x=520, y=10)
box5 = Spinbox(frame, from_=1, to=49, width=2, font=("Ariel", 30))
box5.place(x=670, y=10)
box6 = Spinbox(frame, from_=1, to=49, width=2, font=("Ariel", 30))
box6.place(x=820, y=10)


# GENERATING RANDOM NUMBERS
def submit():
    playsound("DrumrollSound Effect.mp3")
    numbers = list(range(1, 50))
    random.shuffle(numbers)
    draw = numbers[:6]

    box7["state"] = "normal"
    box7.delete(0, END)
    box7.insert(0, draw[0])
    box7["state"] = "readonly"

    box8["state"] = "normal"
    box8.delete(0, END)
    box8.insert(0, draw[1])
    box8["state"] = "readonly"

    box9["state"] = "normal"
    box9.delete(0, END)
    box9.insert(0, draw[2])
    box9["state"] = "readonly"

    box10["state"] = "normal"
    box10.delete(0, END)
    box10.insert(0, draw[3])
    box10["state"] = "readonly"

    box11["state"] = "normal"
    box11.delete(0, END)
    box11.insert(0, draw[4])
    box11["state"] = "readonly"

    box12["state"] = "normal"
    box12.delete(0, END)
    box12.insert(0, draw[5])
    box12["state"] = "readonly"


# PLAY BUTTON
play = Button(root, bg="#212529", fg="#f0e68c", font="50", text="PLAY", command=submit)
play.place(x=465, y=300)

# LABEL BOX
frame = LabelFrame(root, width=950, height=100, text="Winning Numbers", bg="#49af62")
frame.place(x=25, y=380)

# ENTRIES
box7 = Entry(frame, text="box7", width=2, font=("Ariel", 30), state="readonly")
box7.place(x=70, y=10)
box8 = Entry(frame, width=2, font=("Ariel", 30), state="readonly")
box8.place(x=230, y=10)
box9 = Entry(frame, width=2, font=("Ariel", 30), state="readonly")
box9.place(x=370, y=10)
box10 = Entry(frame, width=2, font=("Ariel", 30), state="readonly")
box10.place(x=520, y=10)
box11 = Entry(frame, width=2, font=("Ariel", 30), state="readonly")
box11.place(x=670, y=10)
box12 = Entry(frame, width=2, font=("Ariel", 30), state="readonly")
box12.place(x=820, y=10)


# DEFINING CLEAR BUTTON FUNCTION
def clear():
    playsound("ha.mp3")
    box.delete(0, 'end')
    box2.delete(0, 'end')
    box3.delete(0, 'end')
    box4.delete(0, 'end')
    box5.delete(0, 'end')
    box6.delete(0, 'end')
    box7["state"] = "normal"
    box7.delete(0, END)
    box7["state"] = "readonly"

    box8["state"] = "normal"
    box8.delete(0, END)
    box8["state"] = "readonly"

    box9["state"] = "normal"
    box9.delete(0, END)
    box9["state"] = "readonly"

    box10["state"] = "normal"
    box10.delete(0, END)
    box10["state"] = "readonly"

    box11["state"] = "normal"
    box11.delete(0, END)
    box11["state"] = "readonly"

    box12["state"] = "normal"
    box12.delete(0, END)
    box12["state"] = "readonly"


# DEFINING EXIT BUTTON FUNCTION
def destroy():
    playsound("alert.mp3")
    msg = messagebox.askquestion("Gone So Soon", "Are You Sure You Would Like To Exit ?")
    if msg == "yes":
        root.destroy()


# DEFINING CLAIM BUTTON FUNCTION
def claim():
    playsound("winner.mp3")
    messagebox.showinfo("CONGRATULATIONS", "!!!! YOU'RE A WINNER !!!!")
    root.destroy()
    import bank


# PLAY AGAIN BUTTON
play_again = Button(root, text="PLAY AGAIN", bg="#212529", fg="#f0e68c", font="50", command=submit)
play_again.place(x=40, y=550)
# CLAIM BUTTON
claim = Button(root, text="CLAIM", bg="#212529", fg="#f0e68c", font="50", command=claim)
claim.place(x=350, y=550)
# CLEAR BUTTON
clear_btn = Button(root, text="CLEAR", bg="#212529", fg="#f0e68c", font="50", command=clear)
clear_btn.place(x=650, y=550)
# EXIT BUTTON
exit_btn = Button(root, text="EXIT", bg="#212529", fg="#f0e68c", font="50", command=destroy)
exit_btn.place(x=900, y=550)

# RUN CODE
root.mainloop()
