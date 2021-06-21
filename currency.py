# BANKING DETAILS TESTING
from tkinter import *
from tkinter import messagebox
from playsound import playsound
import requests

root = Tk()
root.title("CURRENCY CONVERTER")  # WINDOW TITLE
root.geometry("1000x600")  # WINDOW SIZE
root.config(bg="#ffbe0b")  # WINDOW COLOR
root.resizable(False, False)  # NON RESIZEABLE

# LOTTO IMAGE
img = PhotoImage(file="lotto.png")
Label(root, image=img).place(x=410, y=20)  # LOTTO IMAGE PLACEMENT

value = IntVar()

# API FOR CURRENCY EXCHANGE RATE
info = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/ZAR')
info_json = info.json()

conversion_rate = info_json['conversion_rates']

# LABEL
val_label = Label(root, text="Value: ", bg="#212529", fg="#f0e68c", font=("Ariel", 15))
val_label.place(x=465, y=110)

# AMOUNT YOU WANT TO EXCHANGE
val_entry = Entry(root, textvariable=value, bg="#212529", fg="#f0e68c", font=("Ariel", 15))
val_entry.place(x=370, y=150)

# LABEL
from_label = Label(root, text="From: ZAR", bg="#212529", fg="#f0e68c", font=("Ariel", 15))
from_label.place(x=445, y=190)

# LABEL
convert = Label(root, text="To: ", bg="#212529", fg="#f0e68c", font=("Ariel", 15))
convert.place(x=480, y=230)

# LIST OF CURRENCIES
con_list = Listbox(root, width=20)
for i in conversion_rate.keys():
    con_list.insert(END, str(i))
    con_list.config(bg="#212529", fg="#f0e68c", font=("Ariel", 15))
    con_list.place(x=250, y=270)

con_label = Label(root, text="Result: ", bg="#212529", fg="#f0e68c", font=("Ariel", 15))
con_label.place(x=700, y=350)


# CONVERSION DEFINITION OF FUNCTIONS
def convert_currency():
    num = float(val_entry.get())
    print(info_json['conversion_rates'][con_list.get(ACTIVE)])
    ans = num * info_json['conversion_rates'][con_list.get(ACTIVE)]
    con_label['text'] = ans


# BACK BUTTON DEFINITION
def go_back():
    msg = messagebox.askquestion("GO BACK", "Would You Like To Go Back To The Previous Page ?")
    if msg == "yes":
        root.destroy()
        import bank


# EXIT BUTTON DEFINITION
def exit_page():
    msg = messagebox.askquestion("EXIT", "Are You Sure You Would Like To Exit ?")
    if msg == "yes":
        root.destroy()


def remover():
    val_entry.delete(0, END)


remove = Button(root, text="Clear", bg="#212529", fg="#f0e68c", font=("Ariel", 15), command=remover)
remove.place(x=600, y=550)
# CONVERSION  BUTTON PLACEMENT AND COLOR
con_btn = Button(root, command=convert_currency, text="Convert", bg="#212529", fg="#f0e68c", font=("Ariel", 15))
con_btn.place(x=294, y=550)
# BACK BUTTON PLACEMENT AND COLOR
back = Button(root, text="Go Back", bg="#212529", fg="#f0e68c", font=("Ariel", 15), command=go_back)
back.place(x=407, y=550)
# EXIT BUTTON PLACEMENT AND COLOR
exit = Button(root, text="Exit", bg="#212529", fg="#f0e68c", font=("Ariel", 15), command=exit_page)
exit.place(x=525, y=550)

# RUN CODE
root.mainloop()
