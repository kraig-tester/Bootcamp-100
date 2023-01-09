import random
import pandas as pd

# #List comprehension
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     new_list.append(n+1)

# print(new_list)

# new_list = [n+1 for n in numbers]
# print(new_list)

# name = "Angela"
# new_name = [letter for letter in name]
# print(new_name)

# doubled_list = [num * 2 for num in range(1,5)]
# print(doubled_list)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)


# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# long_names = [name.upper() for name in names if len(name) > 4]
# print(long_names)

# students_scores = {student:random.randint(0,100) for student in names}
# print(students_scores)

# passed_students  = {student:score for (student, score) in students_scores.items() if score >= 60}
# print(passed_students)

student_dict = {
    "student": ["Igor", "Sasha", "Andrei"],
    "scores": [80, 70, 75]
}

for (key, value) in student_dict.items():
    print(key)

student_df = pd.DataFrame(student_dict)
# print(student_df)

for (index, row) in student_df.iterrows():
    print(row.student)