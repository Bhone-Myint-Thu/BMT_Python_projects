# Input the number of students
n = int(input("Number of Students:"))

# Input the student records
records = []
for _ in range(n):
    name = input("Name:")
    grade = float(input("Grade:"))
    records.append([name, grade])

# Find the second lowest grade
grades = sorted(set([record[1] for record in records]))
second_lowest_grade = grades[1]

# Get the names of students with the second lowest grade
second_lowest_students = [record[0] for record in records if record[1] == second_lowest_grade]

# Sort the names alphabetically
second_lowest_students.sort()

# Print each name on a new line
for student in second_lowest_students:
    print("Second Lowest:",student)
