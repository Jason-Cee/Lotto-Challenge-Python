# BANKING DETAILS TESTING
import tkinter
from tkinter import *
from tkinter import messagebox
from playsound import playsound

root = Tk()
root.title("BANKING DETAILS")  # WINDOW TITLE
root.geometry("1000x600")  # WINDOW SIZE
root.config(bg="#ffbe0b")  # WINDOW COLOR
root.resizable(False, False)  # NON RESIZEABLE

# LOTTO IMAGE
img = PhotoImage(file="lotto.png")
Label(root, image=img).place(x=410, y=20)  # LOTTO IMAGE PLACEMENT


class BankDetails:

    def __init__(self, window):
        # HEADING
        self.bankdet = Label(root, text="BANKING DETAILS", bg="#212529", fg="#f0e68c", font=("Ariel", 30))
        self.bankdet.place(x=310, y=130)

        # ACCOUNT DETAILS
        # DIFFERENT BANKING OPTIONS
        self.stock_txt = "Select Bank: "
        self.stock_var = tkinter.StringVar(value=self.stock_txt)
        self.optmenu = OptionMenu(root, self.stock_var, "Capitec", "Standard Bank", "First National Bank", "ABSA",
                                  "BidVest",
                                  "Nedbank")
        self.optmenu.config(bg="#212529", fg="#f0e68c", font=("Ariel", 15))
        self.optmenu.place(x=410, y=200)

        # ACCOUNT HOLDER LABEL
        self.account = Label(root, text="Account Holder: ", bg="#212529", fg="#f0e68c", font=("Ariel", 15))
        self.account.place(x=250, y=300)
        # ACCOUNT HOLDER ENTRY
        self.acc_ent = Entry(root, bg="#212529", fg="#f0e68c", font=("Ariel", 15))
        self.acc_ent.place(x=500, y=300)

        self.accnum = Label(root, text="Account Number: ", bg="#212529", fg="#f0e68c", font=("Ariel", 15))
        self.accnum.place(x=250, y=360)
        # ACCOUNT NUMBER ENTRY
        self.accnumb = Entry(root, bg="#212529", fg="#f0e68c", font=("Ariel", 15))
        self.accnumb.place(x=500, y=360)

        # BRANCH CODE LABEL
        self.branch = Label(root, text="Branch Code: ", bg="#212529", fg="#f0e68c", font=("Ariel", 15))
        self.branch.place(x=250, y=420)
        # BRANCH CODE ENTRY
        self.code = Entry(root, bg="#212529", fg="#f0e68c", font=("Ariel", 15))
        self.code.place(x=500, y=420)

        # DEFINING SUBMIT BUTTON FUNCTION
        self.submit = Button(root, text=" Submit ", bg="#212529", fg="#f0e68c", font=("Ariel", 15), command=self.accnt)
        self.submit.place(x=100, y=500)

        # STYLING OF CLEAR BUTTON
        self.clear = Button(root, text=" Clear ", bg="#212529", fg="#f0e68c", font=("Ariel", 15), command=self.delete)
        self.clear.place(x=600, y=500)

        # STYLING AND PLACEMENT OF EXIT BUTTON
        self.exitbtn = Button(root, text=" Exit ", bg="#212529", fg="#f0e68c", font=("Ariel", 15), command=self.destroy)
        self.exitbtn.place(x=820, y=500)
        # STYLING AND PLACEMENT OF CONVERT BUTTON
        self.currency = Button(root, text="Convert", bg="#212529", fg="#f0e68c", font=("Ariel", 15), command=self.
                               convert)
        self.currency.place(x=350, y=500)

    def accnt(self):
        self.accnumber = self.accnumb.get()
        self.acc_name = self.acc_ent.get()

        if not self.acc_name.isalpha():
            messagebox.showerror("INVALID", "PLEASE ENTER PROPER NAME")

        elif not self.accnumber.isdigit():
            messagebox.showerror("INVALID", "PLEASE ENTER VALID ACCOUNT NUMBER")

        elif not self.code.isdigit():
            messagebox.showerror("INVALID", "PLEASE ENTER VALID BRANCH CODE")

    # DEFINING CLEAR BUTTON FUNCTION
    def delete(self):
        self.acc_ent.delete(0, 'end')
        self.accnumb.delete(0, 'end')
        self.code.delete(0, 'end')
        playsound("ha.mp3")

    # DEFINING EXIT BUTTON FUNCTION
    def destroy(self):
        playsound("alert.mp3")
        msg = messagebox.askquestion("Gone So Soon", "Are You Sure You Would Like To Exit ?")
        if msg == "yes":
            root.destroy()

    def convert(self):
        msg = messagebox.askquestion("CONVERSION", "YOU ARE ABOUT TO GO TO THE CURRENCY CONVERTER")
        if msg == "yes":
            root.destroy()
            import currency


run = BankDetails(root)

root.mainloop()
