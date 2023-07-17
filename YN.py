# Accept a number from the user
number = int(input("Enter a number from 1 to 7: "))

# Accept whether the student has a medical cause or not
medical_cause = input("Do you have a medical cause? (Y/N): ")

# Map the number to the name of the day
day_name = ""
if number == 1:
    day_name = "Sunday"
elif number == 2:
    day_name = "Monday"
elif number == 3:
    day_name = "Tuesday"
elif number == 4:
    day_name = "Wednesday"
elif number == 5:
    day_name = "Thursday"
elif number == 6:
    day_name = "Friday"
elif number == 7:
    day_name = "Saturday"
else:
    print("Invalid number entered. Please enter a number from 1 to 7.")

# Check if the student can sit based on the day and medical cause
if day_name != "":
    if day_name == "Sunday" or day_name == "Saturday":
        print("You can sit on", day_name)
    elif medical_cause == 'Y':
        print("You can sit on", day_name, "due to a medical cause.")
    else:
        print("You cannot sit on", day_name, "without a medical cause.")
