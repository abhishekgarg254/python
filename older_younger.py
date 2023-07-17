# Accept the ages of three people from the user
age1 = int(input("Enter the age of person 1: "))
age2 = int(input("Enter the age of person 2: "))
age3 = int(input("Enter the age of person 3: "))

# Determine the oldest and youngest ages
oldest = max(age1, age2, age3)
youngest = min(age1, age2, age3)

# Print the oldest and youngest ages
print("The oldest person is", oldest, "years old.")
print("The youngest person is", youngest, "years old.")
