# Student Grade Management System

print("================================")
print("     STUDENT GRADE SYSTEM")
print("================================")

# Get student information
name = input("Enter student name: ")

# Get marks
math = float(input("Enter Mathematics mark: "))
english = float(input("Enter English mark: "))
python = float(input("Enter Python mark: "))
database = float(input("Enter Database mark: "))

# Calculate total and average
total = math + english + python + database
average = total / 4

# Determine grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Determine result
if average >= 50:
    result = "PASS"
else:
    result = "FAIL"

# Display report
print("\n========== STUDENT REPORT ==========")
print("Student Name:", name)
print("------------------------------------")
print("Mathematics:", math)
print("English:", english)
print("Python:", python)
print("Database:", database)
print("------------------------------------")
print("Total Marks:", total, "/ 400")
print("Average:", round(average, 2))
print("Grade:", grade)
print("Result:", result)
print("====================================")