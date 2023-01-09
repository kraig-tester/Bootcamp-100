from ctypes import alignment
import tkinter as tk
import pandas as pd
from random import choice

FILE_PATH = "data/german_1000.csv"
FILE_TO_LEARN = "data/words_to_learn.csv"
FONT_LANGUAGE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
BACKGROUND_COLOR = "#B1DDC6"
MAIN_LANGUAGE = "English"
SECONDARY_LANGUAGE = "German"
words_to_learn = {}
current_card = {}
timer = None


def swap_side():
    canvas.itemconfig(l_language, text=MAIN_LANGUAGE, fill="white")
    canvas.itemconfig(l_word, text=f"{current_card[MAIN_LANGUAGE]}", fill="white")
    canvas.itemconfig(c_image, image=image_back)


def load_new_word():
    global current_card, timer
    window.after_cancel(timer)
    current_card = choice(words_to_learn)
    canvas.itemconfig(l_language, text=SECONDARY_LANGUAGE, fill="black")
    canvas.itemconfig(l_word, text=f"{current_card[SECONDARY_LANGUAGE]}", fill="black")
    canvas.itemconfig(c_image, image=image_front)
    timer = window.after(3000, func=swap_side)


def is_known():
    words_to_learn.remove(current_card)
    data = pd.DataFrame(words_to_learn)
    data.to_csv(FILE_TO_LEARN, index=False)
    load_new_word()

try:
    words_dataframe = pd.read_csv(FILE_TO_LEARN)
except FileNotFoundError:
    words_dataframe = pd.read_csv(FILE_PATH)
finally:    
    words_to_learn = words_dataframe.to_dict(orient="records")

window = tk.Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

timer = window.after(3000, func=swap_side)

image_front = tk.PhotoImage(file="images/card_front.png")
image_back = tk.PhotoImage(file="images/card_back.png")
image_wrong = tk.PhotoImage(file="images/wrong.png")
image_right = tk.PhotoImage(file="images/right.png")

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
c_image = canvas.create_image(400,263, image=image_front)
canvas.grid(column=0,row=0,columnspan=2)

l_language = canvas.create_text(400, 150, font=FONT_LANGUAGE)
l_word = canvas.create_text(400, 263, font=FONT_WORD,)
b_wrong = tk.Button(image=image_wrong,highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR, command=load_new_word)
b_wrong.grid(column=0, row=1)

b_right = tk.Button(image=image_right,highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR, command=is_known)
b_right.grid(column=1, row=1)

load_new_word()

window.mainloop()