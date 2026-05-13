# from tabulate import tabulate
#
# subjects_list = ["Maths", "English", "Chemistry", "Physics"]
#
# def collect_student_scores():
#     student_records = []
#     while True:
#         student_name = input("Enter student name (or 'stop' to finish): ").strip()
#         if student_name.lower() == "stop":
#             break
#         if not student_name.isalpha():
#             print("Name must only contain letters.")
#             continue
#
#         subject_scores = []
#         for subject in subjects_list:
#             while True:
#                 score_input = input(f"{subject} score for {student_name}: ")
#                 if score_input.isdigit():
#                     score_value = int(score_input)
#                     if 0 <= score_value <= 100:
#                         subject_scores.append(score_value)
#                         break
#                     else:
#                         print("Score must be between 0 and 100.")
#                 else:
#                     print("Please enter a number.")
#         student_records.append([student_name] + subject_scores)
#     return student_records
#
#
#
# def calculate_grade(average_score):
#     if average_score >= 90: return "A"
#     elif average_score >= 80: return "B"
#     elif average_score >= 70: return "C"
#     elif average_score >= 60: return "D"
#     else: return "F"
#
#
#
# def calculate_average(student_record):
#     scores = student_record[1:]
#     return sum(scores) / len(subjects_list)
#
#
#
# def sort_student_records(student_records):
#     return sorted(student_records, key=calculate_average, reverse=True)
#
#
#
# def display_results(student_records):
#     sorted_records = sort_student_records(student_records)
#     results_table = []
#     for record in sorted_records:
#         avg_score = calculate_average(record)
#         row = record + [round(avg_score, 2), calculate_grade(avg_score)]
#         results_table.append(row)
#
#     headers = ["Name"] + subjects_list + ["Average", "Grade"]
#     print(tabulate(results_table, headers=headers, tablefmt="grid"))
#
# students_data = collect_student_scores()
# display_results(students_data)



