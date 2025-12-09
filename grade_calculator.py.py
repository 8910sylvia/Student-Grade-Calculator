# Student Grade Calculator

marks = float(input("Enter the student's marks(0-100): "))

if marks >= 90:
    grade = "A"
    message = "Excellent work! Keep shining!"
elif marks >= 80:
    grade = "B"
    message = "Great job! Keep it up!"
elif marks >= 70:
    grade = "C"
    message = "Good effort! Keep improving!"
elif marks >= 60:
    grade = "D"
    message = "You are almost there, keep working hard!"
else:
    grade = "F"
    message = "Don't give up! Learn and come back stronger!"

print("\n---- Result ----")
print(f"Grade: {grade}")
print(f"Message: {message}")


    