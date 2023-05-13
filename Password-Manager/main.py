from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    random_letters = [choice(letters) for _ in range(randint(8, 10))]
    random_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    random_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = random_letters + random_numbers + random_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    email = email_user_entry.get()
    password = password_entry.get()
    website = website_entry.get()

    data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if email == "" or password == "" or website == "":
        messagebox.showwarning(title="Not all credentials entered", message="Do not leave ANY boxes empty!")
        return

    try:
        with open("data.json", mode="r") as file:
            original_data = (json.load(file))
    except FileNotFoundError:
        with open("data.json", mode="w") as data_file:
            json.dump(data, data_file, indent=4)
    else:
        original_data.update(data)

        with open("data.json", mode="w") as file:
            json.dump(original_data, file, indent=4)
    finally:
        clear()


def find_password():
    try:
        with open("data.json", mode="r") as file:
            total_data = json.load(file)
            try:
                website_data = total_data[website_entry.get()]
            except KeyError:
                messagebox.showwarning(title=website_entry.get(), message="DATA DOES NOT EXIST")
            else:
                messagebox.showinfo(title=website_entry.get(), message=f"Email: {website_data['email']}\nPassword: "
                                                                       f"{website_data['password']}")
    except FileNotFoundError:
        messagebox.showwarning(title="File does not exist", message="You have not added ANY data.")


def clear():
    password_entry.delete(0, END)
    website_entry.delete(0, END)

    website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=30)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(width=14, command=find_password, text="Search")
search_button.grid(row=1, column=2)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(row=2, column=0)

email_user_entry = Entry(width=48)
email_user_entry.grid(row=2, column=1, columnspan=2)
email_user_entry.insert(0, "yugsha28@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=30)
password_entry.grid(row=3, column=1, columnspan=1)

generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(row=3, column=2)

add_password_button = Button(text="Add", width=42, command=save)
add_password_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
