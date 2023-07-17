# Accept the percentage from the user
percentage = float(input("Enter the percentage: "))

# Determine the grade based on the percentage
if percentage > 90:
    grade = "A"
elif percentage > 80:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "D"

# Display the grade
print("Your grade is:", grade)
