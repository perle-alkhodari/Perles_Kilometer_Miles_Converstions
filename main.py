from Converter import Converter
import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox

var = 0
convert = Converter()


def switch_choice():
    global var
    var += 1

    if var % 2 == 0:
        convert_choice.config(text="K")

    else:
        convert_choice.config(text="M")


def _convert():
    global convert
    global var

    try:
        if int(userEntry.get()) >= 0:
            if var % 2 == 0:
                result_label.config(text=str(convert.km_to_miles(float(userEntry.get()))))

            else:
                result_label.config(text=str(convert.miles_to_km(float(userEntry.get()))))
        else:
            messagebox.showinfo("Invalid", "Please enter a valid number")
    except:
        m = messagebox.showinfo("Invalid", "Please enter a number")

window = tb.Window(themename="superhero")
window.geometry("400x200")
window.title("Converter")

title_label = tb.Label(
    window,
    text="Km/Miles converter",
    font=("Futura", 25, "bold"),
)
title_label.grid(row=0, column=0, columnspan=3, pady=20)

convert_choice = tb.Button(
    window,
    text="K",
    width=2,
    command=switch_choice
)
convert_choice.grid(row=1, column=0, sticky=E, padx=(30, 0))

userEntry = tb.Entry(
    window,
)
userEntry.grid(row=1, column=1, sticky=EW, padx=10)

submit_button = tb.Button(
    window,
    text="Convert",
    command=_convert
)
submit_button.grid(row=1, column=2, sticky=W)

result_label = tb.Label(
    window,
    text="",
    font=("Futura", 20)
    )
result_label.grid(row=2, column=0, columnspan=3, pady=20)

window.mainloop()
