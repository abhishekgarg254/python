# Accept a number from the user
number = int(input("Enter a number: "))

# Get the last digit of the number
last_digit = number % 10

# Check if the last digit is divisible by 3
if last_digit % 3 == 0:
    print("The last digit is divisible by 3.")
else:
    print("The last digit is not divisible by 3.")
