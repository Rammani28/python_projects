# miles to kilometer converter
from cgitb import text
from tkinter import *

FONT = ("Arial", 24, "bold")

window = Tk()
window.title("Miles to KM converter")
window.config(pady=50, padx=50)

is_equal_to = Label(text="is equal to ")
is_equal_to.config(font=FONT, padx=20, pady=20)
is_equal_to.grid(column=0, row=1)

km = Label(text="km", font=FONT, padx=20, pady=20)
km.grid(column=2, row=1)

miles = Label(text="Miles", font=FONT, padx=20, pady=20)
miles.grid(column=2, row=0)

km_label = Label(text='0', font=FONT)
km_label.grid(column=1, row=1)

mile_entry_box = Entry(width=10, font=FONT)
mile_entry_box.insert(END, string="0")
mile_entry_box.grid(column=1, row=0)


def convert_mile_to_km():
    km_label.config(text=f"{round(1.61 * float(mile_entry_box.get()), 2)}")


calculate_button = Button(text="calculate", font=FONT, command=convert_mile_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()