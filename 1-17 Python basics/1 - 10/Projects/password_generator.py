#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_password_list = []
for i in range(1, nr_letters + 1):
    #easy_password_list += random.choice(letters)
    easy_password_list += letters[random.randint(0, len(letters) - 1)]

for i in range(1, nr_symbols + 1):
    easy_password_list += symbols[random.randint(0, len(symbols) - 1)]

for i in range(1, nr_numbers + 1):
    easy_password_list += numbers[random.randint(0, len(numbers) - 1)]

#print(f"Here is your easy password: {easy_password_list}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password_list = easy_password_list

random.shuffle(hard_password_list)

hard_password = ""
for char in hard_password_list:
    hard_password += char
print(f"Here is your password: {hard_password}")