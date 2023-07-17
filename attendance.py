# Accept the number of classes held and attended from the user
classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

# Calculate the percentage of classes attended
attendance_percentage = (classes_attended / classes_held) * 100

# Check if the student is allowed to sit in the exam
if attendance_percentage >= 75:
    print("Percentage of classes attended:", attendance_percentage)
    print("You are allowed to sit in the exam.")
else:
    print("Percentage of classes attended:", attendance_percentage)
    print("You are not allowed to sit in the exam.")
