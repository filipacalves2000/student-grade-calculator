name = input("Enter the student's name: ")

grade1 = float(input("Enter first grade: "))
grade2 = float(input("Enter second grade: "))
grade3 = float(input("Enter third grade: "))

average = (grade1 + grade2 + grade3) / 3

print("Student:", name)
print("Final average:", average)

if average >= 10:
    print("Passed")
else:
    print("Failed")