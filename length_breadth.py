# Accept the length and breadth from the user
length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))

# Check if it is a square or rectangle
if length == breadth:
    print("It is a square.")
else:
    print("It is a rectangle.")
