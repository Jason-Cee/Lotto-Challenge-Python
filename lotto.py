# IMPORTS NEEDED TO RUN MY CODE
import re
from tkinter import *
from tkinter import messagebox
from playsound import playsound
import datetime
from datetime import *
import random

root = Tk()
root.title("Lotto Verification")  # WINDOW TITLE
root.geometry("1000x600")  # WINDOW SIZE
root.config(bg="#ffbe0b")  # WINDOW COLOR
root.resizable(False, False)  # NON RESIZEABLE

# TIME AND DATE
now = datetime.now()

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
box2.place(x=220, y=10)
box3 = Spinbox(frame, from_=1, to=49, width=2, font=("Ariel", 30))
box3.place(x=370, y=10)
box4 = Spinbox(frame, from_=1, to=49, width=2, font=("Ariel", 30))
box4.place(x=520, y=10)
box5 = Spinbox(frame, from_=1, to=49, width=2, font=("Ariel", 30))
box5.place(x=670, y=10)
box6 = Spinbox(frame, from_=1, to=49, width=2, font=("Ariel", 30))
box6.place(x=820, y=10)


# GENERATING RANDOM NUMBERS
def plays():
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

    play["state"] = "disabled"
    play_again["state"] = "normal"

    # GETTING INPUT LIST AND GENERATED LIST TO COMPARE AND CHECK IF USER WON ANYTHING
    numbers1 = [int(box.get()), int(box2.get()), int(box3.get()), int(box4.get()), int(box5.get()), int(box6.get())]
    numbers2 = draw
    comp = (set(numbers1).intersection(numbers2))
    results = len(comp)
    messagebox.showinfo("!!!! WINNINGS !!!!", "You Got " + str(results) + " Winning Ball(s)")
    prize = {6: "R10 000  000.00", 5: "R8584.00", 4: "R2384.00", 3: "R100.50", 2: "R20.00", 1: "R00.00", 0: "R00.00"}
    y = {prize.get(results)}

    # APPENDING TEXT
    with open("track.txt", "a+") as w:
        w.write("User Lotto Numbers: " + str(numbers1) + "\n")
        w.write("Generated Lotto Numbers: " + str(draw) + "\n")
        w.write("Total Winnings: " + str(y) + "\n")
        w.write("Played Lotto at: " + str(now) + "\n")
        w.write("\n")
        w.close()

    if results <= 1:
        playsound("alert.mp3")
        messagebox.showinfo("Unlucky", "You Have Won R0.00")
    elif results == 2:
        playsound("youwin.mp3")
        messagebox.showinfo("LUCKY", "You Have Won R20.00")  # PRIZE 1
        messagebox.askquestion("LUCKY", "Would You Like To Claim ?")
        if "yes":
            root.destroy()
        import bank
    elif results == 3:
        playsound("youwin.mp3")
        messagebox.showinfo("LUCKY", "You Have Won R100.50")  # PRIZE 2
        messagebox.askquestion("LUCKY", "Would You Like To Claim ?")
        if "yes":
            root.destroy()
        import bank
    elif results == 4:
        playsound("youwin.mp3")
        messagebox.showinfo("LUCKY", "You Have Won R2384.00")  # PRIZE 3
        messagebox.askquestion("LUCKY", "Would You Like To Claim ?")
        if "yes":
            root.destroy()
        import bank
    elif results == 5:
        playsound("youwin.mp3")
        messagebox.showinfo("LUCKY", "You Have Won R8584.00")  # PRIZE 4
        messagebox.askquestion("LUCKY", "Would You Like To Claim ?")
        if "yes":
            root.destroy()
        import bank
    else:
        playsound("slot.mp3")
        messagebox.showinfo("!!!! JACKPOT !!!!", "YOU HAVE WON THE JACKPOT")  # PRIZE 5
        messagebox.showinfo("!!!! JACKPOT !!!!", "You Have Won R10 000 000")
        messagebox.askquestion("LUCKY", "Would You Like To Claim ?")
        if "yes":
            root.destroy()
        import bank


# PLAY BUTTON
play = Button(root, bg="#212529", fg="#f0e68c", font="50", text="PLAY", command=plays)
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

    play["state"] = "normal"
    play_again["state"] = "disabled"


# DEFINING EXIT BUTTON FUNCTION
def close():
    playsound("alert.mp3")
    msg = messagebox.askquestion("Gone So Soon", "Are You Sure You Would Like To Exit ?")
    if msg == "yes":
        root.destroy()


# # DEFINING PLAY AGAIN BUTTON
def plays_again():
    msg = messagebox.askquestion("RETRY", "Would You Like To Select New Numbers ?")
    if msg == "yes":
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

    play["state"] = "normal"
    play_again["state"] = "disabled"


# PLAY AGAIN BUTTON
play_again = Button(root, text="PLAY AGAIN", bg="#212529", fg="#f0e68c", font="50", command=plays_again)
play_again.place(x=40, y=550)
# CLEAR BUTTON
clear_btn = Button(root, text="CLEAR", bg="#212529", fg="#f0e68c", font="50", command=clear)
clear_btn.place(x=650, y=550)
# EXIT BUTTON
exit_btn = Button(root, text="EXIT", bg="#212529", fg="#f0e68c", font="50", command=close)
exit_btn.place(x=900, y=550)

# IF PLAY BUTTON IS ACTIVATED, PLAY AGAIN BUTTON WILL BE DEACTIVATED
play["state"] = "normal"
play_again["state"] = "disabled"

# RUN CODE
root.mainloop()
