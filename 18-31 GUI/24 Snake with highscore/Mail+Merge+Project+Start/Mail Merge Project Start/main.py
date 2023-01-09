#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

OUTPUT_PATH = "C:/Users/laone/Desktop/Studies/Python/Bootcamp/24 snake with highscore/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/"
FILE_PATH = "C:/Users/laone/Desktop/Studies/Python/Bootcamp/24 snake with highscore/Mail+Merge+Project+Start/Mail Merge Project Start/Input/"

contents = ""
with open(FILE_PATH + "Letters/starting_letter.txt") as file_letter:
    contents = file_letter.read()
    
    with open(FILE_PATH + "Names/invited_names.txt") as file_names:
        for name in file_names.readlines():
            with open(OUTPUT_PATH + f"letter_to_{name.strip()}.txt", "w") as new_letter:
                new_contents = contents.replace("[name]", name.strip())
                new_letter.write(new_contents)
