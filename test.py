# # class BankDetails:
# #
# #     def __init__(self, window):
# #         # HEADING
# #         self.bankdet = Label(root, text="BANKING DETAILS", bg="#212529", fg="#f0e68c", font=("Ariel", 30))
# #         self.bankdet.place(x=310, y=130)
# #
# #         # ACCOUNT DETAILS
# #         # DIFFERENT BANKING OPTIONS
# #         self.stock_txt = "Select Bank: "
# #         self.stock_var = tkinter.StringVar(value=self.stock_txt)
# #         self.optmenu = OptionMenu(root, self.stock_var, "Capitec", "Standard Bank", "First National Bank", "ABSA",
# #                                   "BidVest",
# #                                   "Nedbank")
# #
# #
# # run = BankDetails(root)
# #
# # root.mainloop()
#
#
# # All the imports
# from tkinter import *
# from tkinter import messagebox
# import requests
#
# # Let's start with the design of the GUI
# root = Tk()
# root.title("Currency Conversion")
# root.geometry("300x600")
# root.config(bg="#6a040f")
# root.resizable(False, False)
#
# value = IntVar()
#
# # Retrieving information from external JSON file
# info = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/USD')
# info_json = info.json()
#
# conversion_rate = info_json['conversion_rates']
#
# # label and entry for the results
# val_label = Label(root, text="Value", font="50")
# val_label.config(bg="#6a040f", fg="#f1e05a")
# val_label.place(x=130, y=10)
#
# val_entry = Entry(root, textvariable=value)
# val_entry.config(bg="yellow")
# val_entry.place(x=70, y=50)
#
# # Creating the FROM (Standard value is USD)
# from_label = Label(root, text="From: USD", font="30")
# from_label.config(bg="#6a040f", fg="#f1e05a")
# from_label.place(x=110, y=100)
#
# # Conversion of the data with the loop
# convert = Label(root, text="To:", font="30")
# convert.config(bg="#6a040f", fg="#f1e05a")
# convert.place(x=140, y=150)

#
# # Defining Currency Conversion
# def convert_currency():
#     num = float(val_entry.get())
#     print(info_json['conversion_rates'][con_list.get(ACTIVE)])
#     ans = num * info_json['conversion_rates'][con_list.get(ACTIVE)]
#     con_label['text'] = ans

#
# root.mainloop()


import unittest

import main
import lotto
import currency


class Submit(unittest.TestCase):

    def test_success(self):
        a_style = main.success
        self.assertTrue(a_style, "True")

    def test_plays(self):
        b_style = lotto.plays
        self.assertTrue(b_style, "True")

    def test_plays_again(self):
        c_style = lotto.plays_again
        self.assertTrue(c_style, "True")

    def test_convert(self):
        d_style = currency.convert_currency
        self.assertTrue(d_style, "True")


class Clear(unittest.TestCase):

    def test_delete(self):
        e_style = main.delete
        self.assertTrue(e_style, "True")

    def test_clear(self):
        f_style = lotto.clear
        self.assertTrue(f_style, "True")

    def test_remover(self):
        g_style = currency.remover
        self.assertTrue(g_style, "True")


class Exit(unittest.TestCase):

    def test_out(self):
        h_style = main.out
        self.assertTrue(h_style, "True")

    def test_close(self):
        i_style = lotto.close
        self.assertTrue(i_style, "True")

    def test_exit_page(self):
        j_style = currency.exit_page
        self.assertTrue(j_style, "True")
