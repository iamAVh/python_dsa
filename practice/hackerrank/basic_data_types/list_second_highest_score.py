students = []
n = int(input("enter how many students: "))

for i in range(n):
    name = input("enter the name: ")
    grade= float(input("enter the grade: "))
    students.append([name, grade])


grades = sorted(set(student[1] for student in students))
second_lowest = grades[1]

for student in sorted(students):
    if student[1] == second_lowest:
        print(student[0])
