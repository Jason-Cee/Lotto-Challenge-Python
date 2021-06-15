import tkinter
from tkinter import *
from tkinter import messagebox
from playsound import playsound

# playsound("winner.mp3")

root = Tk()
root.title("BANKING DETAILS")  # WINDOW TITLE
root.geometry("1000x600")  # WINDOW SIZE
root.config(bg="#ffbe0b")  # WINDOW COLOR
root.resizable(False, False)  # NON RESIZEABLE

# LOTTO IMAGE
img = PhotoImage(file="lotto.png")
Label(root, image=img).place(x=410, y=20)  # LOTTO IMAGE PLACEMENT

# HEADING
bankdet = Label(root, text="BANKING DETAILS", bg="#212529", fg="#f0e68c", font=("Ariel", 30))
bankdet.place(x=310, y=130)

# ACCOUNT DETAILS
# DIFFERENT BANKING OPTIONS
stock_txt = "Select Bank: "
stock_var = tkinter.StringVar(value=stock_txt)
optmenu = OptionMenu(root, stock_var, "Capitec", "Standard Bank", "First National Bank", "ABSA", "BidVest", "Nedbank")
optmenu.config(bg="#212529", fg="#f0e68c", font=("Ariel", 15))
optmenu.place(x=410, y=200)

# ACCOUNT HOLDER LABEL
account = Label(root, text="Account Holder: ", bg="#212529", fg="#f0e68c", font=("Ariel", 15))
account.place(x=250, y=300)
# ACCOUNT HOLDER ENTRY
acc_ent = Entry(root, bg="#212529", fg="#f0e68c", font=("Ariel", 15))
acc_ent.place(x=500, y=300)


# DEFINING ACCOUNT ENTRY FUNCTION
def accnt():
    accnumber = accnumb.get()
    acc_name = acc_ent.get()

    if not accnumber.isdigit():
        messagebox.showerror("ERROR", "Invalid Entry")

    elif not code.isdigit():
        messagebox.showerror("ERROR", "Invalid Entry")

    elif not acc_name.isalpha():
        messagebox.showerror("ERROR", "Invalid Entry")


# ACCOUNT NUMBER LABEL
accnum = Label(root, text="Account Number: ", bg="#212529", fg="#f0e68c", font=("Ariel", 15))
accnum.place(x=250, y=360)
# ACCOUNT NUMBER ENTRY
accnumb = Entry(root, bg="#212529", fg="#f0e68c", font=("Ariel", 15))
accnumb.place(x=500, y=360)

# BRANCH CODE LABEL
branch = Label(root, text="Branch Code: ", bg="#212529", fg="#f0e68c", font=("Ariel", 15))
branch.place(x=250, y=420)
# BRANCH CODE ENTRY
code = Entry(root, bg="#212529", fg="#f0e68c", font=("Ariel", 15))
code.place(x=500, y=420)

# DEFINING SUBMIT BUTTON FUNCTION
submit = Button(root, text=" Submit ", bg="#212529", fg="#f0e68c", font=("Ariel", 15), command=accnt)
submit.place(x=100, y=500)


# DEFINING CLEAR BUTTON FUNCTION
def delete():
    acc_ent.delete(0, 'end')
    accnumb.delete(0, 'end')
    code.delete(0, 'end')
    playsound("ha.mp3")

# STYLING OF CLEAR BUTTON
clear = Button(root, text=" Clear ", bg="#212529", fg="#f0e68c", font=("Ariel", 15), command=delete)
clear.place(x=470, y=500)


# DEFINING EXIT BUTTON FUNCTION
def destroy():
    playsound("alert.mp3")
    msg = messagebox.askquestion("Gone So Soon", "Are You Sure You Would Like To Exit ?")
    if msg == "yes":
        root.destroy()


exitbtn = Button(root, text=" Exit ", bg="#212529", fg="#f0e68c", font=("Ariel", 15), command=destroy)
exitbtn.place(x=820, y=500)

root.mainloop()
