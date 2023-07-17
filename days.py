# Accept a number from the user
number = int(input("Enter a number from 1 to 7: "))

# the number to the name of the day
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

# Display the name of the day
if day_name != "":
    print("The day corresponding to the number", number, "is", day_name)
