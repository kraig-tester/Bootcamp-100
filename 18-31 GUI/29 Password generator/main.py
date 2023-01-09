from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip

EMAIL = "ikrasnyanskiy123@gmail.com"
FONT = ("Arial", 10, "normal")
PASSWORD_FILE = "data.txt"
IMG_PATH_RELATIVE = "logo.png"

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    password_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    password_symbols = [choice(NUMBERS) for _ in range(randint(2, 4))]
    password_numbers = [choice(SYMBOLS) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    e_password.insert(0, password)
    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = e_website.get()
    e_mail = e_email.get()
    password = e_password.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty fields", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are details entered:\nEmail: {e_mail}\nPassword: {password}\nIs it ok?")

        if is_ok:
            with open(PASSWORD_FILE,"a") as file:
                # print(f"{e_website.get()} | {e_email.get()} | {e_password.get()}")
                file.write(f"{website} | {e_mail} | {password}\n")

                # print("Added to file.")
                e_website.delete(0,END)
                e_password.delete(0,END)

        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50)

canvas = Canvas(width=200,height=200)
password_image = PhotoImage(file=IMG_PATH_RELATIVE)
canvas.create_image(100,100,image=password_image)
canvas.grid(column=1,row=0)

l_website = Label(text="Website")
l_website.grid(column=0,row=1)
l_email = Label(text="Email/Username:")
l_email.grid(column=0,row=2)
l_password = Label(text="Password:")
l_password.grid(column=0,row=3)

e_website = Entry(width=40)
e_website.grid(column=1,row=1,columnspan=2)
e_website.focus()

e_email = Entry(width=40)
e_email.grid(column=1,row=2,columnspan=2)
e_email.insert(0, EMAIL)

e_password = Entry(width=22)
e_password.grid(column=1,row=3)

b_generate = Button(text="Generate password", command=generate_password)
b_generate.grid(column=2,row=3)

b_add = Button(text="Add", command=save_password, width=36)
b_add.grid(column=1,row=4, columnspan=2)

window.mainloop()