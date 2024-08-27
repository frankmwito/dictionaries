# extract a student with the highest grade value from a dictionary with student names as keys and their scores as values

students = { }
num = int(input("Enter size of your dictionary:"))

for i in range(num):
    name = input(f"Enter student name {i+1}:")
    scores = int(input(f"Enter the respective score {i+1}:"))
    students.update({name: scores})

print(students)

max_score = max(students.values())
for key, value in students.items():
    if value == max_score:
        print(f"The student with the highest score is: {key} with a score of {value}")