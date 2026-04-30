# student_names = []
# subjects = ["Maths", "English", "Chemistry", "Physics"]
# scores = []
#
# while True:
#     name = input("Please enter your name (or type stop to stop): ")
#     if name == "stop":
#         break
#     student_names.append(name)
#
#     student_scores = []
#     for subject in subjects:
#         score = int(input(f"Enter {subject} score for {name}: "))
#         student_scores.append(score)
#     scores.append(student_scores)
#
# print("Student Names:", student_names)
# print("Scores:", scores)

#
# student_names = []
# subjects = ["Maths", "English", "Chemistry", "Physics"]
# scores = []
#
# while True:
#     name = input("Please enter your name (or type stop to stop): ")
#     if name == "stop":
#         break
#     student_names.append(name)
#
#     student_scores = []
#     for subject in subjects:
#         score = int(input(f"Enter {subject} score for {name}: "))
#         student_scores.append(score)
#     scores.append(student_scores)
#
# print(f"{'Name':<10}", end="")
# for subject in subjects:
#     print(f"{subject:<10}", end="")
# print()
#
# for i in range(len(student_names)):
#     print(f"{student_names[i]:<10}", end="")
#     for score in scores[i]:
#         print(f"{score:<10}", end="")
#     print()



from tabulate import tabulate

student_names = []
subjects = ["Maths", "English", "Chemistry", "Physics"]
scores = []

while True:
    name = input("Please enter your name (or type stop to stop): ")
    if name.lower() == "stop":
        break
    student_names.append(name)

    student_scores = []
    for subject in subjects:
        score = int(input(f"Enter {subject} score for {name}: "))
        student_scores.append(score)
    scores.append(student_scores)

table_data = []
for i in range(len(student_names)):
    avg_score = sum(scores[i]) / len(scores[i])
    row = [student_names[i]] + scores[i] + [round(avg_score, 2)]
    table_data.append(row)

headers = ["Name"] + subjects + ["Average"]

print(tabulate(table_data, headers=headers, tablefmt="grid"))
