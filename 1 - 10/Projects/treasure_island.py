print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇

action1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right".\n')

if action1.lower() == "left":

    action2 = input('You\'ve come to a lake. There is an island in the middle of the lake? Type "wait" to wait for a boat. Type "swim" to swim across.\n')

    if action2.lower() == "wait":
        action3 = input('You\'ve arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue? Which colour do you choose?\n')

        if action3.lower() == "yellow":
            print("You have found the treasure! You win!")
        elif action3.lower() == "red":
            print("You've been burnt by fire!\nGame over.")
        elif action3.lower() == "blue":
            print("You've entered a room full of beast!\nGame over.")
        else:
            print("You've chosen wrong door!\nGame over.")

    else:
        print("You could not resist the flow.\nGame Over.")

else:
    print("You fell into a hole.\nGame Over.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
