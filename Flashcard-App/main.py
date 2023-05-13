from tkinter import *
import pandas
from random import choice

# data
data_file = pandas.read_csv("data/hindi_words.csv")
data = data_file.to_dict(orient="records")

# variables
BACKGROUND_COLOR = "#B1DDC6"
random_word = {"None": "None"}
word_to_display = None

# basic setup
window = Tk()
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
window.title("Flashy")


# functions
def generate_random_word():
    global word_to_display, random_word, cover_up, flip_timer
    flash_card.after_cancel(flip_timer)
    random_word = choice(data)
    word_to_display = random_word["Hindi"]
    cover_up = flash_card.create_rectangle([0, 180, 770, 380], fill="white", outline="white")
    flash_card.itemconfig(word_text, text=word_to_display)
    flash_card.tag_raise(word_text)

    flip_timer = flash_card.after(5000, switch_english)


def right():
    generate_random_word()
    switch_hindi()


def wrong():
    generate_random_word()
    switch_hindi()


def switch_english():
    flash_card.itemconfig(card, image=flash_card_img_back)
    flash_card.itemconfig(word_text, text=random_word["English"], fill="white")
    flash_card.itemconfig(language_text, text="English", fill="white")
    flash_card.itemconfig(cover_up, fill="#91C2AF", outline="#91C2AF")


def switch_hindi():
    flash_card.itemconfig(card, image=flash_card_img_front)
    flash_card.itemconfig(word_text, text=random_word["Hindi"], fill="black")
    flash_card.itemconfig(language_text, text="Hindi", fill="black")
    flash_card.itemconfig(cover_up, fill="white", outline="white")


# actual flash card
flash_card_img_front = PhotoImage(file="images/card_front.png")
flash_card_img_back = PhotoImage(file="images/card_back.png")
flash_card = Canvas(highlightthickness=0, height=526, width=800, bg=BACKGROUND_COLOR)
card = flash_card.create_image(400, 263, image=flash_card_img_front)

# flash card text
language_text = flash_card.create_text(400, 150, text="Hindi", fill="black", font=("Calibri", 40, "italic"))
word_text = flash_card.create_text(400, 263, text="", fill="black", font=("Calibri", 60, "bold"))

# putting flashcard canvas on screen
flash_card.grid(row=0, column=0, columnspan=2)

# correct button
checkmark_img = PhotoImage(file="images/right.png")
correct_button = Button(image=checkmark_img, highlightthickness=0, bg=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR,
                        borderwidth=0, command=right, activebackground=BACKGROUND_COLOR)
correct_button.grid(column=0, row=1)

# wrong button
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR,
                      borderwidth=0, command=wrong, activebackground=BACKGROUND_COLOR)
wrong_button.grid(column=1, row=1)

# generate a random word from the list
flip_timer = flash_card.after(5000, switch_english)
generate_random_word()

# mainloop
window.mainloop()
