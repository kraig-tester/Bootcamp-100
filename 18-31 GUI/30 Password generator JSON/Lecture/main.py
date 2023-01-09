
# # try except else finally
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"Key": "Value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     print("File does not exist.\nCreating a file")
#     file = open("a_file.txt", "w")
#     file.write("Content")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     print("File was closed")
#     file.close()
#     raise TypeError("My error")

# #FileNotFoundError
# with open("some_file.txt") as file:
#     file.read()

# #KeyError
# a_dictionary = {"Key": "Value"}
# value = a_dictionary["Non_existent_key"]

# #IndexError
# fruits_list = ["Apple", "Banana", "Mango"]
# mango = fruits_list[3]

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
    
bmi = weight/height ** 2
print(f"BMI: {bmi}")
