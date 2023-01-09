alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(user_text, shift, direction):
    shift_multiplier = 0
    if direction == "encode":
        shift_multiplier = 1
    elif direction == "decode":
        shift_multiplier = -1

    if shift_multiplier != 0:
        final_text = ""

        for letter in user_text:
            if letter not in alphabet:
                final_text += letter
                continue 

            index_to_shift = alphabet.index(letter) + shift*shift_multiplier
            
            if index_to_shift < 0:
                final_text += alphabet[index_to_shift + 26]
            elif index_to_shift > 25:
                final_text += alphabet[index_to_shift - 26]
            else:
                final_text += alphabet[index_to_shift]

        print(f"\nThe {direction}d text is '{final_text}'.\n")

    else:
        print("Wrong command, please try again")

running = True

while running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'exit' to quit the program:\n")
    if direction.lower() == "exit":
        break

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if shift >= 26:
        shift = shift%26

    caesar(text, shift, direction.lower())