FILE_NAME = "de_full.txt"
NUM_OF_WORDS = 1000
LANGUAGE = "german"

with open(FILE_NAME) as file:
    contents = ""
    for _ in range(NUM_OF_WORDS):
        new_line = file.readline()
        contents += new_line.strip().split()[0] + "\n"

with open(f"{LANGUAGE}_{NUM_OF_WORDS}.txt", "w") as file:
    file.write(contents)
    print(f"File {file.name} has been created.")
