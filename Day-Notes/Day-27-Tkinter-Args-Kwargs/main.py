from tkinter import *

window = Tk()
window.minsize(width=500, height=300)

# label

my_label = Label(text="Text", font=("Consolas", 24, "bold"))

my_label["text"] = "New Text"
my_label.config(text="New Text")

# my_label.pack()  # adding keyword parameters such as "expand=True" or "side='left'" can affect where it is positioned

# my_label.place(x=100, y=40)

my_label.grid(column=1, row=2, columnspan=2)
window.grid_columnconfigure(2,weight=1)  # column 10 will grow
window.grid_rowconfigure(2,weight=1)  # row 15 will grow


# Button

def button_clicked():
    my_label["text"] = input.get()


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, columnspan=2, row=2, sticky="N")

# Entry

input = Entry(width=10)


window.mainloop()
