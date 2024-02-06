import tkinter as tk
from tkinter import *


def entrynumber():
      entrynumber = inputBox.get()
      if entrynumber == "*123#":
            print(mtn_ussd())
      elif entrynumber == "*200#":
            print(etisalat_ussd())
      elif entrynumber == "*500#":
            print(glo_ussd())
      elif entrynumber == "*121#":
            print(airtel_ussd())
      else:
            print(
                  'invalid ussd'
            )


ussd = tk.Tk(screenName='ussd')
ussd.geometry('250x390')
ussd.title('PHONE')
displayframe = Frame(ussd)
displayframe.pack()

inputBox = tk.Entry(ussd, font='system', bd=5, bg='gray', justify=CENTER)

textarea = Text(displayframe, width=30, height=10, bg='seashell3', font='system', bd=5)
textarea.grid()
dailpad_frame = Frame(ussd)

number ={
     'one': "1",
     'two': "2",
     'three': '3',
     'four': "4",
     'five': "5",
     'six': '6',
     'seven': '7',
     'eight': "8",
     'nine': '9',
     'zero': "0",
     'hash': "#",
     'asteric': '*'
      }


def one():
      one = '1'
      inputBox.insert(30, one)


def two():
      two = '2'
      inputBox.insert(30, two)


def three():
      three = '3'
      inputBox.insert(30, three)


def four():
      four = '4'
      inputBox.insert(30, four)


def five():
      five = '5'
      inputBox.insert(30, five)


def six():
      six = '6'
      inputBox.insert(30, six)


def seven():
      seven = '7'
      inputBox.insert(30, seven)


def eight():
      eight = '8'
      inputBox.insert(30, eight)


def nine():
      nine = '9'
      inputBox.insert(30, nine)


def zero():
      zero = '0'
      inputBox.insert(30, zero)


def hash():
      hash = '#'
      inputBox.insert(30, hash)


def star():
      star = '*'
      inputBox.insert(30, star)


Button1 = tk.Button(dailpad_frame, text="1", width=10, bd=3, bg='coral2', pady=5, command=one)
Button2 = tk.Button(dailpad_frame, text="2", width=10, bd=3, bg='coral2', pady=5, padx=3, command=two)
Button3 = tk.Button(dailpad_frame, text="3", width=10, bd=3, bg='coral2', pady=5, command=three)
Button4 = tk.Button(dailpad_frame, text="4", width=10, bd=3, bg='coral2', pady=5, command=four)
Button5 = tk.Button(dailpad_frame, text="5", width=10, bd=3, bg='coral2', pady=5, padx=3, command=five)
Button6 = tk.Button(dailpad_frame, text="6", width=10, bd=3, bg='coral2', pady=5, command=six)
Button7 = tk.Button(dailpad_frame, text="7", width=10, bd=3, bg='coral2', pady=5, command=seven)
Button8 = tk.Button(dailpad_frame, text="8", width=10, bd=3, bg='coral2', pady=5, padx=3, command=eight)
Button9 = tk.Button(dailpad_frame, text="9", width=10, bd=3, bg='coral2', pady=5, command=nine)
ButtonStar = tk.Button(dailpad_frame, text="*", width=10, bd=3, bg='coral2', pady=5, command=star)
Button0 = tk.Button(dailpad_frame, text="0", width=10, bd=3, bg='coral2', pady=5, padx=3, command=zero)
ButtonHash = tk.Button(dailpad_frame, text="#", width=10, bd=3, bg='coral2', pady=5, command=hash)


sendButton = tk.Button(dailpad_frame, text="send", width=10, bd=3, bg='deep sky blue', pady=10, command=entrynumber)

Button1.grid(row=1, column=1)
Button2.grid(row=1, column=2)
Button3.grid(row=1, column=3)
Button4.grid(row=2, column=1)
Button5.grid(row=2, column=2)
Button6.grid(row=2, column=3)
Button7.grid(row=3, column=1)
Button8.grid(row=3, column=2)
Button9.grid(row=3, column=3)
ButtonStar.grid(row=4, column=1)
Button0.grid(row=4, column=2)
ButtonHash.grid(row=4, column=3)
sendButton.grid(row=5, column=2)
inputBox.pack(fill=X)
dailpad_frame.pack(fill=X)
ussd.mainloop()

