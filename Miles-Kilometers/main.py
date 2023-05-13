from tkinter import *

window = Tk()
window.minsize(200, 100)
window.config(padx=20, pady=20)


def calculate():
    miles = mile_entry.get()
    km = int(float(miles) * 1.609)
    km_display.config(text=km)


mile_entry = Entry(width=7)
mile_entry.grid(row=1, column=2)

mile_label = Label(text="Mile(s)")
mile_label.grid(row=1, column=3)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=2, column=1)

km_display = Label(text=0)
km_display.grid(row=2, column=2)

km_label = Label(text="Km")
km_label.grid(row=2, column=3)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=3, column=2)

window.mainloop()
